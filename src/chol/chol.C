#include <cstdlib>
#include <cmath>
#include <iostream>
#include <omp.h>
#include <mkl.h>

double cov(double x, double y)
{
  return std::exp(-0.5 * std::abs(x - y));
}

int main(int argc, char ** argv)
{
  if (argc != 3) {
    std::cerr << "Usage: chol <num_threads> <matrix_size>" << std::endl;
    return 1;
  }

  omp_set_num_threads(atoi(argv[1]));

  double L = 1.0;
  unsigned int N = atoi(argv[2]);
  double dx = (double) L / (N - 1);

  double * A = (double *)malloc(N * N * sizeof(double));
  for (unsigned int i = 0; i < N; i++) {
    for (unsigned int j = 0; j < N; j++) {
      A[i*N+j] = cov(i*dx, j*dx);
    }
  }

  double start = omp_get_wtime();

  // We're letting MKL choose the workspace array at runtime
  // Assume unsigned int N converts to lapack_int
  int info = LAPACKE_dpotrf(LAPACK_ROW_MAJOR, 'U', N, A, N);

  double time = omp_get_wtime() - start;

  std::cout << "LAPACKE_dpotrf executed in " << time << " secs." << std::endl;

  std::cout << "LAPACKE_dpotrf return value is: " << info << std::endl;

  free(A);
  return info;
}
