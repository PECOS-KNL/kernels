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
  if (argc != 4) {
    std::cerr << "Usage: gp <num_threads> <queso_input_file> <num_simulations>" << std::endl;
    return 1;
  }

  // Initialise MPI with threading support.
  int required = MPI_THREAD_SERIALIZED;
  int provided;
  MPI_Init_thread(&argc, &argv, required, &provided);

  // Fail if the provided support is not the required support
  if (provided != required) {
    queso_error_msg("This MPI implementation provides insufficient threading support");
  }

  omp_set_num_threads(atoi(argv[1]));

  // Step 0 of 5: Set up environment
  QUESO::FullEnvironment * env = new QUESO::FullEnvironment(MPI_COMM_WORLD, argv[2], "", NULL);

  // Step 1 of 5: Instantiate the parameter space
  QUESO::VectorSpace<> paramSpace(*env, "param_", 1, NULL);

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
  unsigned int num_simulations = atoi(argv[3]);
  Likelihood<> lhood("llhd_", paramDomain, num_simulations);

  QUESO::GslVector point(paramSpace.zeroVector());

  double start_time = omp_get_wtime();
  lhood.lnValue(point, NULL, NULL, NULL, NULL);
  double time = omp_get_wtime() - start_time;

  // Open a file
  unsigned int num_openmp = atoi(argv[1]);
  int num_mpi = env->fullComm().NumProc();
  int rank = env->fullRank();

  std::ostringstream filename;
  filename << "submit_all_ddr/time_mpi_" << num_mpi << "_openmp_" << num_openmp << "_rank_" << rank << ".txt";

  std::ofstream output_file(filename.str());
  output_file << "Likelihood evaluation took " << time << " secs." << std::endl;
  output_file.close();

  MPI_Finalize();

  return 0;
}
