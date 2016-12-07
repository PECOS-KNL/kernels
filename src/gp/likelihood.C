#include "likelihood.h"

#include <queso/GslVector.h>
#include <queso/GslMatrix.h>

template <class V, class M>
Likelihood<V, M>::Likelihood(const char * prefix,
    const QUESO::VectorSet<V, M> & domainSet)
  : QUESO::BaseScalarFunction(prefix, domainSet)
{
  // Do nothing
}

template <class V, class M>
Likelihood<V, M>::~Likelihood()
{
  // Do nothing
}

template <class V, class M>
double
Likelihood<V, M>::lnValue(const V & domainVector, const V * domainDirection,
    V * gradVector, M * hessianMatrix, V * hessianEffect) const
{
  // Construct Gaussian likelihood and do a cholesky
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
