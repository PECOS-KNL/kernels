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



Cores_256=[1, 2, 4, 8, 16, 32, 64, 128, 256]
Cores_128=[1, 2, 4, 8, 16, 32, 64, 128]
Cores_64=[1, 2, 4, 8, 16, 32, 64]

CPU_256=[86.0533051, 35.8494295, 15.6884386, 8.7995897, 3.4137126, 2.0844045, 1.6152648, 1.6390807, 1.4453344]
CPU_128=[78.8591899, 31.5992704, 12.5380067, 8.7481251, 3.609148, 2.0546135, 1.9851383, 2.0864243]
CPU_64=[74.4944213, 27.9063423, 10.7003363, 5.691174, 2.9290911, 2.7930199, 2.6874417]





fig=plt.figure(1,figsize=(6,4))
plt.plot(Cores_64,CPU_64,'b-o',label=r'MPI$\times$OpenMP=64')
plt.plot(Cores_128,CPU_128,'r-s',label=r'MPI$\times$OpenMP=128')
plt.plot(Cores_256,CPU_256,'g-^',label=r'MPI$\times$OpenMP=256')
plt.xscale('log')
plt.xlim([0.5,512])
plt.yscale('log')
plt.legend(frameon=False,numpoints=1,fontsize=12)
plt.xticks(Cores_256)
xlabels = ["1","2","4",  "8",  "16",  "32",  "64","128","256"]

fig.gca().set_xticklabels(xlabels)
plt.xlabel('MPI tasks')
plt.ylabel('Elapsed  time (sec)')
plt.savefig('DNS_Parallelism.pdf',bbox_inches='tight')
plt.close()
