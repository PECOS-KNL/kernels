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
# rcParams['xtick.labelsize']=30
# rcParams['ytick.labelsize']=30
# rcParams['contour.negative_linestyle'] = 'solid'



Cores=[1, 2, 4, 8, 16, 32, 64, 128, 256]
FFT_OMP=[44.73466, 23.28606, 12.65032, 6.41637, 3.239718, 1.663566, 0.877158, 0.842224, 0.9406795]
FFT_MPI=[44.73466, 23.20402, 11.74475, 5.905075, 3.244862, 1.501264, 0.827825, 0.8068079, 0.940958]
FFT_IDEAL=[44.73466, 22.36733, 11.183665, 5.5918325, 2.79591625, 1.397958125, 0.698979063, 0.349489531, 0.174744766]
WAVE_OMP=[130.65, 66.0438, 35.0373, 17.6006, 8.87388, 4.46213, 2.32496, 1.67509, 1.71673]
WAVE_MPI=[130.65, 68.8252, 34.4125, 17.22, 8.67876, 4.35679, 2.21419, 1.40401, 1.21734]
WAVE_IDEAL=[130.65, 65.325, 32.6625, 16.33125, 8.165625, 4.0828125, 2.04140625, 1.020703125, 0.510351563]


fig=plt.figure(1,figsize=(6,4))
plt.plot(Cores,FFT_OMP,'b-o',label='FFT (OpenMP)')
plt.plot(Cores,FFT_MPI,'m-^',label='FFT (MPI)')
plt.plot(Cores,WAVE_OMP,'r-D',label='Solve N-S eq (OpenMP)')
plt.plot(Cores,WAVE_MPI,'g-s',label='Solve N-S eq (MPI)')
plt.plot(Cores,FFT_IDEAL,'k--',label='Linear Scalability')
plt.plot(Cores,WAVE_IDEAL,'k--')
plt.xscale('log')
plt.xlim([0.5,512])
plt.yscale('log')
plt.legend(frameon=False,numpoints=1,fontsize=12)
plt.xticks(Cores)
xlabels = ["1","2","4",  "8",  "16",  "32",  "64","128","256"]

fig.gca().set_xticklabels(xlabels)
plt.xlabel('MPI tasks or OpenMP threads')
plt.ylabel('Elapsed  time (sec)')
plt.savefig('DNS_FFT_Wave.pdf',bbox_inches='tight')
plt.close()
