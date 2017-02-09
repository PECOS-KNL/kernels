header = """#!/bin/bash
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
"""

footer = """
echo -n "End: "
date
"""

n = [1, 2, 4, 8, 16, 32, 64, 128, 256]

for i in n:
    for j in n:
        num_openmp = i
        num_mpi = j
        if num_mpi * num_openmp <= 256:
	    filename = "submit_mpi_" + str(num_mpi) + "_openmp_" + str(num_openmp) + ".sh"
            with open(filename, 'w') as file:
                file.write(header)
                job_string = "ibrun -np " + str(num_mpi) + " ./gp " + str(num_openmp) + " queso_input_" + str(num_mpi) + ".txt 5000"
                file.write(job_string)
                file.write(footer)
