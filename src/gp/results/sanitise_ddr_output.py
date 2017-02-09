import numpy as np

def get_all_num_openmp(num_mpi):
    max_num_openmp = 256 / num_mpi  # Want num_openmp * num_mpi <= 256
    num_openmp = 1
    all_num_openmp = []
    while num_openmp <= max_num_openmp:
        all_num_openmp.append(num_openmp)
        num_openmp *= 2
    return all_num_openmp

def sanitise_output(num_mpi, num_openmp):
    for i in range(num_mpi):
        rank = i
        filename = "time_mpi_" + str(num_mpi) + "_openmp_" + str(num_openmp) + "_rank_" + str(i) + ".txt"
        time = 0.0
        with open(filename, 'r') as fp:
            time = fp.read().split()[3]
            print time
        with open(filename + '2', 'w') as fp:
            fp.write(str(time) + '\n');

if __name__ == "__main__":
    all_num_mpi = [1, 2, 4, 8, 16, 32, 64, 128, 256]

    for num_mpi in all_num_mpi:
        all_num_openmp = get_all_num_openmp(num_mpi)
        for num_openmp in all_num_openmp:
            sanitise_output(num_mpi, num_openmp)
