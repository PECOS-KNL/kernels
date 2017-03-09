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

data = np.loadtxt('omp_times.txt')

fig = plt.figure(figsize=(5.5,4))
ax = fig.add_subplot(1, 1, 1)

locator = LogLocator(2)
formatter = LogFormatter(2)

ideal = np.zeros(data.shape[0])
ideal[0] = data[0,1]

for i in range(1, ideal.shape[0]):
    ideal[i] = ideal[i-1] / 2.0

ax.loglog(data[:,0], data[:,1], 'b-x')
ax.loglog(data[:,0], ideal, 'k--')
ax.set_xlim(1, 256)
ax.set_xlabel('OpenMP threads')
ax.set_ylabel('Time to solution (seconds)')
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_minor_locator(NullLocator())
ax.xaxis.set_major_formatter(formatter)
fig.tight_layout()
fig.savefig('openmp_scaling_1.pdf')
ax.cla()
