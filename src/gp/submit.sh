#!/bin/bash
#SBATCH -J gp
#SBATCH -o gp_%j.txt
#SBATCH -n 68
#SBATCH -N 1
#SBATCH -p normal
#SBATCH -t 02:00:00
#SBATCH --mail-user=damon@ices.utexas.edu
#SBATCH --mail-type=begin
#SBATCH --mail-type=end
env
echo -n "Begin: "
date
ibrun -np 1 ./gp 256 queso_input.txt 40000
echo -n "End: "
date
