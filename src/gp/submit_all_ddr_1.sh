#!/bin/bash
sbatch submit_all_ddr/submit_mpi_16_openmp_2.sh
sbatch submit_all_ddr/submit_mpi_16_openmp_1.sh
sbatch results/submit_mpi_16_openmp_16.sh
sbatch results/submit_mpi_128_openmp_2.sh
sbatch results/submit_mpi_128_openmp_1.sh
