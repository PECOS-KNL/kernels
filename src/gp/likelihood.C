#include "likelihood.h"

#include <queso/GslVector.h>
#include <queso/GslMatrix.h>
#include <queso/VectorSet.h>

#include <omp.h>
#include <mkl.h>

#include <cmath>

template <class V, class M>
Likelihood<V, M>::Likelihood(const char * prefix,
    const QUESO::VectorSet<V, M> & domainSet,
    unsigned int num_simulations)
  : QUESO::BaseScalarFunction<V, M>(prefix, domainSet),
    m_observationParameter(1.0),
    m_num_simulations(num_simulations),
    m_simulations(m_num_simulations),
    m_simulationParameters(m_num_simulations),
    m_rho(0.5)
{
  // Generate observational data
  double x = 0.25;  // Observation location
  m_observation = m_observationParameter * std::sin(2.0 * M_PI * x);

  // Generate `simulation data'
  for (unsigned int i = 0; i < m_num_simulations; i++) {
    // Evenly spaced parameters between 0 and 2
    m_simulationParameters[i] = i * 2.0 / (m_num_simulations - 1);
    // Observable is at the same location as the experiment
    m_simulations[i] = m_simulationParameters[i] * std::sin(2.0 * M_PI * x);
  }

  // Allocate memory for the covariance matrix
  // Exceptions will lead to memory leaks.  lul
  m_covariance = (double *)malloc(sizeof(double) *
                                  (m_num_simulations + 1) *
                                  (m_num_simulations + 1));

  if (m_covariance == NULL) {
    queso_error_msg("Could not allocate memory for covariance matrix");
  }
}

template <class V, class M>
Likelihood<V, M>::~Likelihood()
{
  // free(m_covariance);
}

template <class V, class M>
double
Likelihood<V, M>::lnValue(const V & domainVector, const V * domainDirection,
    V * gradVector, M * hessianMatrix, V * hessianEffect) const
{
  double t1 = omp_get_wtime();

  unsigned int total_dim = m_num_simulations + 1;  // Plus 1 for one experiment

  // First, fill up the covariance matrix
#pragma omp parallel for collapse(2)
  for (unsigned int i = 0; i < total_dim; i++) {
    for (unsigned int j = 0; j < total_dim; j++) {
      double parameter1;
      // Deal with the single experiment
      if (i == 0) {
        // Difference in scenario variables is always zero.  No need to handle it.
        // Deal with difference in parameters
        parameter1 = domainVector[0];
      }
      else {
        // Subtract 1 because we have 1 experiment (observation)
        parameter1 = m_simulationParameters[i-1];
      }

      double parameter2;

      // Deal with the single experiment (observation)
      if (j == 0) {
        parameter2 = domainVector[0];
      }
      else {
        // Subtract 1 because we have 1 experiment (observation)
        parameter2 = m_simulationParameters[j-1];
      }

      double param_diff = parameter1 - parameter2;
      m_covariance[i*total_dim+j] = std::pow(m_rho, 4.0 * param_diff * param_diff);

      if (i == j) {
        m_covariance[i*total_dim+j] += 1e-6;
      }
    }
  }

  int info;
  // Compute the \infty-norm of m_covariance
  // All elements of m_covariance are nonnegative
  double norm = 0.0;
  for (unsigned int i = 0; i < total_dim; i++) {
    double tmp = 0.0;

    // Handle element on the diagonal
    tmp += m_covariance[i*total_dim+i];

    for (unsigned int j = i+1; j < total_dim; j++) {
      tmp += 2.0 * m_covariance[i*total_dim+j];
    }

    if (tmp > norm) {
      norm = tmp;
    }
  }

  double t2 = omp_get_wtime();
  double setup_time = t2 - t1;

  // We're letting MKL choose the workspace array at runtime
  // Assume unsigned int N converts to lapack_int
  info = LAPACKE_dpotrf(LAPACK_ROW_MAJOR, 'U', total_dim, m_covariance, total_dim);

  if (info == 0) {
    std::cerr << "LAPACKE_dpotrf was successful" << std::endl;
  }
  else if (info < 0) {
    std::cerr << "LAPACKE_dpotrf was unsuccessful."
              << "  Parameter " << info << " had an illegal value."
              << std::endl;
    queso_error();
  }
  else {  // if (info > 0) {
    std::cerr << "LAPACKE_dpotrf was unseccessful."
              << "  The leading minor of order " << info << " is not pos. def."
              << "  The Cholesky factorisation could not be completed."
              << std::endl;
    queso_error();
  }

  double t3 = omp_get_wtime();
  double factorization_time = t3 - t2;

  // Estimate the condition number of m_covariance
  double cond;
  info = LAPACKE_dpocon(LAPACK_ROW_MAJOR, 'U', total_dim, m_covariance, total_dim, norm, &cond);

  if (info == 0) {
    std::cerr << "Approximate reciprocal condition number of m_covariance is: " << cond << std::endl;
  }
  else {
    std::cerr << "Condition number estimation failed."
              << "  Parameter " << info << " had an illegal value."
              << std::endl;
    queso_error();
  }

  double t4 = omp_get_wtime();
  double condition_num_time = t4 - t3;

  // Now do y^T \Sigma^{-1} y
  // First solve \Sigma x = y for x
  double * y = (double *)malloc(sizeof(double) * total_dim);
  double * x = (double *)malloc(sizeof(double) * total_dim);

  if (x == NULL) {
    std::cerr << "Could not allocate enough memory for rhs" << std::endl;
    queso_error();
  }

  if (y == NULL) {
    std::cerr << "Could not allocate enough memory for data" << std::endl;
    queso_error();
  }

  y[0] = m_observation;
  x[0] = m_observation;
  for (unsigned int i = 0; i < m_num_simulations; i++) {
    y[i+1] = m_simulations[i];
    x[i+1] = m_simulations[i];
  }

  // LAPACK treats the right-hand side as a matrix.  Since we only have one right-hand side
  // the leading dimension of this 'matrix' is 1, not total_dim.  I'm an idiot.
  info = LAPACKE_dpotrs(LAPACK_ROW_MAJOR, 'U', total_dim, 1, m_covariance, total_dim, x, 1);
  if (info == 0) {
    std::cerr << "LAPACKE_dpotrs successful" << std::endl;
  }
  else {
    std::cerr << "LAPACKE_dpotrs unsuccessful.  Parameter " << info << " had an illegal value" << std::endl;
    queso_error();
  }

  double t5 = omp_get_wtime();
  double linear_solve_time = t5 - t4;

  // Second compute y^T x
  double llhd = cblas_ddot(total_dim, y, 1, x, 1);

  double t6 = omp_get_wtime();
  double dot_product_time = t6 - t5;

  std::cout << "Setup \t Fact \t Cond \t Solve \t Dot" << std::endl;

  std::cout << setup_time << "\t"
            << factorization_time << "\t"
            << condition_num_time << "\t"
            << linear_solve_time << "\t"
            << dot_product_time << "\t"
            << std::endl;

  // free(y);
  // free(x);

  return -0.5 * llhd;
}

template <class V, class M>
double
Likelihood<V, M>::actualValue(const V & domainVector,
    const V * domainDirection, V * gradVector, M * hessianMatrix,
    V * hessianEffect) const
{
  return std::exp(this->lnValue(domainVector,
                                domainDirection,
                                gradVector,
                                hessianMatrix,
                                hessianEffect));
}

template class Likelihood<QUESO::GslVector, QUESO::GslMatrix>;
