#!/bin/py
#This python script generate plots of one point statistics with experimental data

import numpy as np
import scipy
import h5py as h5
import math
import glob
import pylab 
import sys
import shutil
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.ticker import MaxNLocator
from numpy import matrix
from numpy import linalg


rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Computer Modern Roman']
rcParams['text.usetex'] = True
# rcParams['xtick.major.size']=20
# rcParams['ytick.major.size']=20
rcParams['xtick.minor.size']=0
# rcParams['ytick.minor.size']=10
rcParams['xtick.labelsize']=10
# rcParams['ytick.labelsize']=30
# rcParams['contour.negative_linestyle'] = 'solid'



Cores=[1, 2, 4, 8, 16, 32, 64, 128, 256]
Elapsed_time=[340.515304,167.247222,83.185743,42.512198,21.1418785,10.6050198,5.7294567,4.1665168,3.6036324]
Ideal=[340.515304,170.257652,85.128826,42.564413,21.2822065,10.64110325,5.320551625,2.660275813,1.330137906]



fig=plt.figure(1,figsize=(6,4))
plt.plot(Cores,Elapsed_time,'b-o',label='Full Timestep')
plt.plot(Cores,Ideal,'k--',label='Linear Scalability')
plt.xscale('log')
plt.xlim([0.5,512])
plt.yscale('log')
plt.legend(frameon=False,numpoints=1,fontsize=12)
plt.xticks(Cores)
xlabels = ["1\n(1x1)","2\n(1x1)","4\n(4x1)",  "8\n(8x1)",  "16\n(16x1)",  "32\n(32x1)",  "64\n(64x1)","128\n(64x2)","256\n(256x1)"]

fig.gca().set_xticklabels(xlabels)
plt.xlabel(r'MPI tasks $\times$ OpenMP threads')
plt.ylabel('Elapsed  time (sec)')
plt.savefig('DNS_full_timestep.pdf',bbox_inches='tight')
plt.close()
