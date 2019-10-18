#!/usr/bin/env python3

import csv
import sys

import  numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


inputfile = '.\data\\' + sys.argv[1]
title = sys.argv[2]

"""basic steps to load in all the data into lists x and y"""
x = []
y = []
with open(inputfile,'r') as datafile:
    datareader = csv.reader(datafile)
    data = list(datareader)                  #load in the data for csv file
row = 1
for i in data[1:]:
    x.append(float(i[0]))
    y.append(float(i[1]))
    row += 1                                 #calculate the number of data groups

x_axis = data[0][0]
y_axis = data[0][1]

"""finish the plotting section"""
linear = np.poly1d(np.polyfit(x,y,deg=1))
x0 = np.arange(0.9*min(x),1.05*max(x),(max(x)-min(x))/100)
fig = plt.figure(figsize = [6.4,6.4])
fig1 = fig.add_subplot(1,1,1)
fig1.plot(x,y,'go',x0,linear(x0),'b-',linewidth = 2,markersize = 6)

"""set some of the tick properties"""
fig1.xaxis.set_ticks_position('bottom')
fig1.yaxis.set_ticks_position('left')
fig1.set_title(title)

"""add labels to axis and scattered spots"""
plt.xlabel(x_axis)
plt.ylabel(y_axis)
plt.text(0.78*max(x),min(y),'y = ' + str(linear).strip(),fontsize = 12)
for i in range(row):
    plt.text(x[i-1],y[i-1],"({} {})".format(str(x[i-1]),str(y[i-1])),\
             fontsize = 8,color = 'red')
#plt.axes(autoscale_on = True)

"""set the limits of axis"""
delta_x = (max(x)-min(x))*0.1
delta_y = (max(y)-min(y))*0.1
x_limit = [min(x)-delta_x,max(x)+delta_x]
y_limit = [min(y)-delta_y,max(y)+delta_y]
plt.xlim(x_limit[0],x_limit[1])
plt.ylim(y_limit[0],y_limit[1])

"""set the minor ticks for x and y axes"""
listx = list(fig1.xaxis.get_majorticklocs())
x_loc_major = listx[1] - listx[0]
x_loc_minor = x_loc_major / 5
x_loc_minor = MultipleLocator(x_loc_minor)

listy = list(fig1.yaxis.get_majorticklocs())
y_loc_major = listy[1] - listy[0]
y_loc_minor = y_loc_major / 5
y_loc_minor = MultipleLocator(y_loc_minor)

fig1.xaxis.set_minor_locator(x_loc_minor)
fig1.yaxis.set_minor_locator(y_loc_minor)

plt.grid(b=True,which='both',axis='both',color='black',linestyle = ":",linewidth = 1)

"""save and show the picture"""
plt.savefig(title+'.png',dpi = 400, bbox_inches = 'tight')
plt.show()
