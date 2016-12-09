#include "likelihood.h"

#include <queso/GenericScalarFunction.h>
#include <queso/GslVector.h>
#include <queso/GslMatrix.h>
#include <queso/UniformVectorRV.h>
#include <queso/StatisticalInverseProblem.h>
#include <queso/ScalarFunction.h>
#include <queso/VectorSet.h>

#include <cstdlib>
#include <cmath>
#include <iostream>
#include <omp.h>

// Forward declaration
int main(int argc, char ** argv)
{
  if (argc != 2) {
    std::cerr << "Usage: gp <queso_input_file>" << std::endl;
    return 1;
  }

  // omp_set_num_threads(atoi(argv[1]));
  // double start = omp_get_wtime();
  // double time = omp_get_wtime() - start;
  // std::cout << "LAPACKE_dpotrf executed in " << time << " secs." << std::endl;

  MPI_Init(&argc, &argv);

  // Step 0 of 5: Set up environment
  QUESO::FullEnvironment env(MPI_COMM_WORLD, argv[1], "", NULL);

  // Step 1 of 5: Instantiate the parameter space
  QUESO::VectorSpace<> paramSpace(env, "param_", 1, NULL);

  double min_val = 0.0;
  double max_val = 1.0;

  // Step 2 of 5: Set up the prior
  QUESO::GslVector paramMins(paramSpace.zeroVector());
  paramMins.cwSet(min_val);
  QUESO::GslVector paramMaxs(paramSpace.zeroVector());
  paramMaxs.cwSet(max_val);

  QUESO::BoxSubset<> paramDomain("param_", paramSpace, paramMins, paramMaxs);

  // Uniform prior here.  Could be a different prior.
  QUESO::UniformVectorRV<> priorRv("prior_", paramDomain);

  // Step 3 of 5: Set up the likelihood using the class above
  Likelihood<> lhood("llhd_", paramDomain);

  // Step 4 of 5: Instantiate the inverse problem
  // QUESO::GenericVectorRV<> postRv("post_", paramSpace);

  // QUESO::StatisticalInverseProblem<> ip("", NULL, priorRv, lhood, postRv);

  // // Step 5 of 5: Solve the inverse problem
  // QUESO::GslVector paramInitials(paramSpace.zeroVector());

  // // Initial condition of the chain
  // paramInitials[0] = 0.0;
  // paramInitials[1] = 0.0;

  // QUESO::GslMatrix proposalCovMatrix(paramSpace.zeroVector());

  // for (unsigned int i = 0; i < 1; i++) {
  //   // Might need to tweak this
  //   proposalCovMatrix(i, i) = 0.1;
  // }

  // ip.solveWithBayesMetropolisHastings(NULL, paramInitials, &proposalCovMatrix);

  MPI_Finalize();

  return 0;
}
