#!/bin/bash
#SBATCH -J chol
#SBATCH -o chol_%j.txt
#SBATCH -n 1
#SBATCH -p development
#SBATCH -t 01:00:00
#SBATCH --mail-user=damon@ices.utexas.edu
#SBATCH --mail-type=begin
#SBATCH --mail-type=end
env
echo -n "Begin: "
date
./chol 288 4096
echo -n "End: "
date
