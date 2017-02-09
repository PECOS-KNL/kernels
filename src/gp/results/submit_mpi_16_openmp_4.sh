#!/bin/bash
#SBATCH -J gp_ddr
#SBATCH -o gp_ddr_%j.txt
#SBATCH -n 272
#SBATCH -N 1
#SBATCH -p normal
#SBATCH -t 48:00:00
#SBATCH --mail-user=damon@ices.utexas.edu
#SBATCH --mail-type=begin
#SBATCH --mail-type=end
env
echo -n "Begin: "
date
export I_MPI_PIN_PROCESSOR_EXCLUDE_LIST=16,17,34,35,84,85,102,103,152,153,170,171,220,221,238,239
export I_MPI_DEBUG=4
export OMP_DISPLAY_ENV=TRUE
ibrun -np 16 ./gp 4 queso_input_16.txt 5000
echo -n "End: "
date
