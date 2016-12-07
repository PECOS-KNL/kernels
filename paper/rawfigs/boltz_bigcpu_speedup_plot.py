#!/usr/bin/python

import sys
import os
import glob

import matplotlib
from matplotlib import rc
rc('text',usetex=True)

# Different modes
# By default, you can "show()" the figure which gives you an interactive window
# and it will save a .png when you call savefig().
# PDF produces a .pdf file, but show() doesn't seem to work.
matplotlib.use("PDF")

import matplotlib.pyplot as plot
from numpy import *

data_do = loadtxt("../data/boltzmann/bigcpu_parado_runtimes.dat", comments="%")
data_task = loadtxt("../data/boltzmann/bigcpu_task_runtimes.dat", comments="%")

total_speedup_do = data_do[0,1]/data_do[:,1]
coll_speedup_do = data_do[0,2]/data_do[:,2]
n_threads_do = data_do[:,0]

total_speedup_task = data_do[0,1]/data_task[:,1]
coll_speedup_task = data_do[0,2]/data_task[:,2]
n_threads_task = data_task[:,0]

fsize=22

tick_label_fontsize=fsize
axis_label_fontsize=fsize
matplotlib.rc('xtick', labelsize=tick_label_fontsize )
#matplotlib.rc(('xtick.major','xtick.minor'),  pad=10)
matplotlib.rc('ytick', labelsize=tick_label_fontsize)

plot.xlabel(r"\# of Threads", fontsize=fsize)
plot.ylabel(r"Speedup Factor",fontsize=fsize)
#plot.title("MIC Speedup",fontsize=16)

lw=3
facecolor="black"
marksize=7

plot.plot( n_threads_do, total_speedup_do, "b-*", label="OMP Do", linewidth=lw, markerfacecolor=facecolor, ms=marksize )
#plot.plot( n_threads_do, coll_speedup_do, "r-*", label="OMP Do CI" )

plot.plot( n_threads_task, total_speedup_task, "b--o", label="OMP Task", linewidth=lw, markerfacecolor=facecolor, ms=marksize )
#plot.plot( n_threads_task, coll_speedup_task, "r--o", label="OMP Task CI" )

plot.plot( [1, 12], [1, 12], "k-", label="Ideal", linewidth=lw, markerfacecolor=facecolor )

plot.axes().set_aspect(0.5)

plot.legend(loc="upper left")
plot.grid(True)

plot.savefig( "boltz_bigcpu_speedup_plot.pdf", bbox_inches='tight' )
plot.show()
