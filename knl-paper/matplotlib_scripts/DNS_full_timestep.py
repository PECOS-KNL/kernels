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

Cores_LS5=[1, 2, 4, 8, 16]
Elapsed_time_LS5=[113.00541,51.381809,24.368666,13.313447,7.637091]
Ideal_LS5=[113.00541,56.502705,28.2513525,14.12567625,7.062838125]

Cores_Big=Cores
Elapsed_time_Big=[1151.88909,571.17865,283.016468,142.313923,69.020769,36.649391,21.211145,15.989299,16.207298]
Ideal_Big=[1151.88909,575.944545,287.9722725,143.9861363,71.99306813,35.99653406,17.99826703,8.999133516,4.499566758]

Cores_LS5_Big=[1,2,4,6,8,12,16,24]
Elapsed_time_LS5_Big=[380.22414,173.10716,82.734204,59.975232,45.998269,33.013729,26.316969,20.488672]
Ideal_LS5_Big=[380.22414,190.11207,95.056035,63.37069,47.5280175,31.685345,23.76400875,15.8426725]


fig=plt.figure(1,figsize=(6,4))
plt.plot(Cores,Elapsed_time,'b-o',label='Stampede-KNL (Small)')
plt.plot(Cores_LS5,Elapsed_time_LS5,'r-s',label='Lonestar5 (Small)')


plt.plot(Cores,Elapsed_time_Big,'g-o',label='Stampede-KNL (Big)')
plt.plot(Cores_LS5_Big,Elapsed_time_LS5_Big,'m-s',label='Lonestar5 (Big)')
plt.plot(Cores_LS5_Big,Ideal_LS5_Big,'k--')
plt.plot(Cores,Ideal,'k--',label='Linear Scalability')
plt.plot(Cores_LS5,Ideal_LS5,'k--')
plt.plot(Cores,Ideal_Big,'k--')

plt.xscale('log')
plt.xlim([0.5,512])
plt.yscale('log')
plt.legend(frameon=False,numpoints=1,fontsize=12)
plt.xticks(Cores)
xlabels = ["CASE\nSmall\nBig","1\n(1x1)\n(1x1)","2\n(2x1)\n(2x1)","4\n(4x1)\n(4x1)",  "8\n(8x1)\n(8x1)",  "16\n(16x1)\n(16x1)",  "32\n(32x1)\n(32x1)",  "64\n(64x1)\n(64x1)","128\n(64x2)\n(128x1)","256\n(256x1)\n(256x1)"]
fig.gca().set_xticks([0.5,1,2,4,8,16,32,64,128,256])
fig.gca().set_xticklabels(xlabels)
plt.xlabel(r'MPI tasks $\times$ OpenMP threads')
plt.ylabel('Elapsed  time (sec)')
plt.savefig('DNS_full_timestep.pdf',bbox_inches='tight')
plt.close()
