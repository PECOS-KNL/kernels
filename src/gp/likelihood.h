#ifndef LIKELIHOOD
#define LIKELIHOOD

#include <queso/ScalarFunction.h>

#include <vector>

// Forward declarations
namespace QUESO
{
  class GslVector;
  class GslMatrix;

  template <class V, class M>
  class VectorSet;
}

template <class V = QUESO::GslVector, class M = QUESO::GslMatrix>
class Likelihood : public QUESO::BaseScalarFunction<V, M>
{
public:
  Likelihood(const char * prefix, const QUESO::VectorSet<V, M> & domainSet);
  virtual ~Likelihood();
  virtual double lnValue(const V & domainVector, const V * domainDirection,
      V * gradVector, M * hessianMatrix, V * hessianEffect) const;
  virtual double actualValue(const V & domainVector, const V * domainDirection,
      V * gradVector, M * hessianMatrix, V * hessianEffect) const;

private:
  // Observational data
  double m_observation;
  double m_observationParameter;

  // Simulation data
  unsigned int m_num_simulations;
  std::vector<double> m_simulations;
  std::vector<double> m_simulationParameters;

  // Correlation strength
  double m_rho;

  // Covariance matrix for the Gaussian Process
  double * m_covariance;
};

#endif  // LIKELIHOOD
