#include "likelihood.h"

#include <queso/GslVector.h>
#include <queso/GslMatrix.h>
#include <queso/VectorSet.h>

#include <cmath>

template <class V, class M>
Likelihood<V, M>::Likelihood(const char * prefix,
    const QUESO::VectorSet<V, M> & domainSet)
  : QUESO::BaseScalarFunction<V, M>(prefix, domainSet),
    m_observationParameter(1.0),
    m_num_simulations(10),
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
  free(m_covariance);
}

template <class V, class M>
double
Likelihood<V, M>::lnValue(const V & domainVector, const V * domainDirection,
    V * gradVector, M * hessianMatrix, V * hessianEffect) const
{
  unsigned int total_dim = m_num_simulations + 1;  // Plus 1 for one experiment

  // First, fill up the covariance matrix
  for (unsigned int i = 0; i < total_dim; i++) {
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

    for (unsigned int j = 0; j < total_dim; j++) {
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
    }
  }

  return 0;
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

template <class V, class M>
double
Likelihood<V, M>::cov(double x, double y)
{
  return std::exp(-0.5 * std::abs(x - y));
}

template class Likelihood<QUESO::GslVector, QUESO::GslMatrix>;
