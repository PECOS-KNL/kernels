import numpy as np
import matplotlib
matplotlib.use('pdf')
from matplotlib import pyplot as plt

from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = 'Computer Modern Roman'
rcParams['text.usetex'] = True

from matplotlib.ticker import LogLocator, NullLocator
from matplotlib.ticker import LogFormatter

fig = plt.figure(figsize=(5.5,4))
ax = fig.add_subplot(1, 1, 1)

locator = LogLocator(2)
formatter = LogFormatter(2)

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

# Generate OpenMP scaling figures
for i in range(times.shape[1]):
    if i == 0 or i == 1:
        ax.loglog(all_ranks, times[:,i], 'b-x')
        ax.set_xlim(1, 256)
        ax.set_xlabel('OpenMP threads')
        ax.set_ylabel('Time to solution (seconds)')
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_minor_locator(NullLocator())
        ax.xaxis.set_major_formatter(formatter)
        fig.tight_layout()
        fig.savefig('openmp_scaling_' + str(all_ranks[i]) + '.pdf')
        ax.cla()
