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

membind_0_data = np.loadtxt('out.membind.0.txt', skiprows=1)
membind_1_data = np.loadtxt('out.membind.1.txt', skiprows=1)

fig = plt.figure(figsize=(5.5,4))
ax = fig.add_subplot(1, 1, 1)

locator = LogLocator(2)
formatter = LogFormatter(2)

threads = [1, 2, 4, 8, 16, 32, 64, 128, 256]

ideal = np.zeros(membind_0_data.shape[0])
ideal[0] = membind_0_data[0,0] + membind_0_data[0,1]

for i in range(1, ideal.shape[0]):
    ideal[i] = ideal[i-1] / 2.0

ax.loglog(threads, membind_0_data[:,0] + membind_0_data[:,1], 'b-o', label='membind=0')
ax.loglog(threads, membind_1_data[:,0] + membind_1_data[:,1], 'r-d', label='membind=1')
ax.loglog(threads, ideal, 'k--', label='Linear Scalability')
ax.set_xlim(0.51, 500)
ax.set_xlabel('OpenMP threads')
ax.set_ylabel('Elapsed time (sec)')
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_minor_locator(NullLocator())
ax.xaxis.set_major_formatter(formatter)
ax.grid(False)
ax.legend(frameon=False, numpoints=1)
fig.tight_layout()
fig.savefig('gp_membind_scaling_collapse.pdf')
ax.cla()
