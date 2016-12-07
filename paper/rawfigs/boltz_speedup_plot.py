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

data_def = loadtxt("../data/boltzmann/mic_def_aff_run_times.dat", comments="%")
data_scat = loadtxt("../data/boltzmann/mic_scat_aff_run_times.dat", comments="%")

total_speedup_def = data_def[0,1]/data_def[:,1]
coll_speedup_def = data_def[0,2]/data_def[:,2]
n_threads_def = data_def[:,0]

total_speedup_scat = data_def[0,1]/data_scat[:,1]
coll_speedup_scat = data_def[0,2]/data_scat[:,2]
n_threads_scat = data_scat[:,0]

fsize=22

tick_label_fontsize=fsize
axis_label_fontsize=fsize
matplotlib.rc('xtick', labelsize=tick_label_fontsize )
#matplotlib.rc(('xtick.major','xtick.minor'),  pad=10)
matplotlib.rc('ytick', labelsize=tick_label_fontsize)

plot.xlabel(r"\# of Threads", fontsize=fsize)
plot.ylabel(r"Speedup Factor",fontsize=fsize)
#plot.title("MIC Speedup",fontsize=fsize)

lw=3
facecolor="black"
marksize=7

plot.axes().set_aspect(2.0)

plot.plot( n_threads_def, total_speedup_def, "b-*", label="Aff=Default", linewidth=lw, markerfacecolor=facecolor, ms=marksize )
#plot.plot( n_threads_def, coll_speedup_def, "r-*", label="Collision Integral", linewidth=lw, markerfacecolor=facecolor )

plot.plot( n_threads_scat, total_speedup_scat, "b--o", label="Aff=scatter", linewidth=lw, markerfacecolor=facecolor, ms=marksize )
#plot.plot( n_threads_scat, coll_speedup_scat, "r--o", label="Collision Integral", linewidth=lw, markerfacecolor=facecolor )

plot.plot( [4, 100], [1, 25], "k-", label="Ideal", linewidth=lw, markerfacecolor=facecolor )

plot.legend(loc="upper left")
plot.grid(True)

plot.savefig( "boltz_speedup_plot.pdf", bbox_inches='tight' )
#plot.show()
