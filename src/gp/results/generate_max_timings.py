import numpy as np
import matplotlib
matplotlib.use('pdf')
from matplotlib import pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

all_ranks = [1, 2, 4, 8, 16, 32, 64, 128, 256]

times = np.zeros((len(all_ranks), len(all_ranks)))
times[:] = np.NAN
for i in range(len(all_ranks)):
    for j in range(len(all_ranks) - i):
        num_openmp = all_ranks[i]
        num_mpi = all_ranks[j]

        with open('time_mpi_' + str(num_mpi) + '_openmp_' + str(num_openmp) + '.txt', 'r') as fp:
            data = [float(time) for time in fp.readlines()]
            times[i,j] = np.max(data)

    print num_openmp, times[i,:]

    # Generate MPI scaling figures
    ax.plot(all_ranks, times[i])
    ax.grid(True)
    fig.savefig('mpi_scaling_' + str(num_openmp) + '.pdf')
    ax.cla()

# Generate OpenMP scaling figures
for i in range(times.shape[1]):
    ax.plot(all_ranks, times[:,i])
    ax.grid(True)
    fig.savefig('openmp_scaling_' + str(all_ranks[i]) + '.pdf')
    ax.cla()
