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


SHUFFLE=[159.981903,72.205867,35.219198,18.19001,8.3375075,4.3540667,2.3130513,1.7662604,1.2844918]
SHUFFLE_IDEAL=[159.981903,79.9909515,39.99547575,19.99773788,9.998868938,4.999434469,2.499717234,1.249858617,0.624929309]
COMM=[5.148741,3.012135,1.809295,1.197113,0.880749,0.3928991,0.3743904,0.3201639,0.1608426]
COMM_IDEAL=[5.148741,2.5743705,1.28718525,0.643592625,0.321796313,0.160898156,0.080449078,0.040224539,0.02011227]


fig=plt.figure(1,figsize=(6,4))
plt.plot(Cores,SHUFFLE,'b-o',label='Data Reorder')
plt.plot(Cores,COMM,'r-^',label='MPI Communication')
plt.plot(Cores,SHUFFLE_IDEAL,'k--',label='Linear Scalability')
plt.plot(Cores,COMM_IDEAL,'k--')
plt.xscale('log')
plt.xlim([0.5,512])
plt.yscale('log')
plt.legend(frameon=False,numpoints=1,fontsize=12)
plt.xticks(Cores)
xlabels = ["1","2","4",  "8",  "16",  "32",  "64","128","256"]
fig.gca().set_xticklabels(xlabels)
plt.xlabel('MPI tasks')
plt.ylabel('Elapsed  time (sec)')
plt.savefig('DNS_Transpose.pdf',bbox_inches='tight')
plt.savefig('DNS_Transpose.eps',bbox_inches='tight')
plt.close()
