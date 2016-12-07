#ifndef LIKELIHOOD
#define LIKELIHOOD

#include <queso/ScalarFunction.h>

// Forward declarations
namespace QUESO
{
  class GslVector;
  class GslMatrix;
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
  double cov(double x, double y);
};

#endif  // LIKELIHOOD
