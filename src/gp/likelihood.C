#include <queso/GslVector.h>
#include <queso/GslMatrix.h>
#include <queso/ScalarFunction.h>

template <class V = QUESO::GslVector, class M = QUESO::GslMatrix>
class Likelihood : public QUESO::BaseScalarFunction<V, M>
{
  Likelihood(const char * prefix, const QUESO::VectorSet<V, M> & domainSet)
    : QUESO::BaseScalarFunction(prefix, domainSet)
  {
  }

  virtual ~Likelihood()
  {
    // Do nothing
  }

  virtual double lnValue(const V & domainVector, const V * domainDirection,
      V * gradVector, M * hessianMatrix, V * hessianEffect)
  {
    return 0;
  }

  virtual double acutalValue(const V & domainVector, const V * domainDirection,
      V * gradVector, M * hessianMatrix, V * hessianEffect)
  {
    return 1;
  }

};
