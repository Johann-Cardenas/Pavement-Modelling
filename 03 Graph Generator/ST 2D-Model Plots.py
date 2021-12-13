# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 14:30:14 2021

@author: Johann Cardenas
"""

import matplotlib
import matplotlib.pyplot as plt 
import numpy as np

#[DEFINE SIZE OF CANVAS]================
plt.rcParams["figure.figsize"] = [10,10]
plt.rcParams["figure.autolayout"] = True

#[DEFINE ARRANGE OF FIGURES 3X3 ]================
fig = plt.figure()
ax1=fig.add_subplot(331)   #Within a 1x1 array, position 1
ax2=fig.add_subplot(332)   #Within a 1x1 array, position 2
ax3=fig.add_subplot(333)   #Within a 1x1 array, position 3
ax4=fig.add_subplot(334)   #Within a 1x1 array, position 4
ax5=fig.add_subplot(335)   #Within a 1x1 array, position 5
ax6=fig.add_subplot(336)   #Within a 1x1 array, position 6
ax7=fig.add_subplot(337)   #Within a 1x1 array, position 7
ax8=fig.add_subplot(338)   #Within a 1x1 array, position 8
ax9=fig.add_subplot(339)   #Within a 1x1 array, position 9


#%%
#[DEFINE MARGINS ]================================
fig.subplots_adjust(top=0.2,bottom=0.15, left=0.2)

#[DEFINE MAIN TITLE ]================================
fig.suptitle('L1 AC125W B600W', fontsize=14, fontweight='bold')

#[DEFINE INPUT DATA ]================================
data= np.loadtxt(fname='S22DATAProcessed.txt', delimiter=',')
print(data)

X=[]
Y=[]
for i in range(len(data)):
    for j in range(2):
        if j==0:
            X.append(data[i][j])
        else:
            Y.append(data[i][j])     
print (X)
print (Y)

#%%
#[FIGURE 1 ]================================
ax1.plot(Y,X,'b',label='S22')    # Plot some data on the axes.
ax1.plot(Y,X,'g-.',label='S22')    # Plot some data on the axes.
ax1.axhline(y=25, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax1.axhline(y=62.5, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax1.axhline(y=125, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax1.axhline(y=275, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 


ax1.set_xlabel('Vertical Stress (MPa)',fontsize=10, fontweight='bold')  # Add an x-label to the axes.
ax1.set_ylabel('Depth (mm)',fontsize=10, fontweight='bold')  # Add a y-label to the axes.
ax1.set_title("Vertical Stress AC",fontsize=10, fontweight='bold')  # Add a title to the axes.
ax1.legend(bbox_to_anchor=(0.05, 0.05, 0.3, 4), loc='lower left',
                      ncol=1, mode="expand", borderaxespad=0.)
ax1.legend(fontsize=9)

ax1.set_xlim(0,-0.8)
ax1.set_ylim(0,750)
ax1.minorticks_on()
ax1.xaxis.grid(True, which='minor')
ax1.yaxis.grid(True, which='minor')
ax1.invert_xaxis()
ax1.invert_yaxis()

ax1.text(-0.475,625, 'S22 Max,AC=-0.69',fontsize=9, style='italic', 
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})
ax1.text(-0.475,705, 'S22 Min,AC=-0.00', fontsize=9, style='italic',
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})

plt.subplots_adjust(bottom=0.1, right=1.5, top=0.8)


#%%
#[FIGURE 2 ]================================
ax2.plot(Y,X,'b',label='S22')    # Plot some data on the axes.
ax2.plot(Y,X,'g-.',label='S22')    # Plot some data on the axes.
ax2.axhline(y=25, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax2.axhline(y=62.5, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax2.axhline(y=125, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax2.axhline(y=275, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 


ax2.set_xlabel('Vertical Stress (MPa)',fontsize=10, fontweight='bold')  # Add an x-label to the axes.
ax2.set_ylabel('Depth (mm)',fontsize=10, fontweight='bold')  # Add a y-label to the axes.
ax2.set_title("Vertical Stress AC",fontsize=10, fontweight='bold')  # Add a title to the axes.
ax2.legend(bbox_to_anchor=(0.05, 0.05, 0.3, 4), loc='lower left',
                      ncol=1, mode="expand", borderaxespad=0.)
ax2.legend(fontsize=9)

ax2.set_xlim(0,-0.8)
ax2.set_ylim(0,750)
ax2.minorticks_on()
ax2.xaxis.grid(True, which='minor')
ax2.yaxis.grid(True, which='minor')
ax2.invert_xaxis()
ax2.invert_yaxis()

ax2.text(-0.475,625, 'S22 Max,AC=-0.69',fontsize=9, style='italic', 
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})
ax2.text(-0.475,705, 'S22 Min,AC=-0.00', fontsize=9, style='italic',
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})

plt.subplots_adjust(bottom=0.1, right=1.5, top=0.8)


#%%
#[FIGURE 3 ]================================
ax3.plot(Y,X,'b',label='S22')    # Plot some data on the axes.
ax3.plot(Y,X,'g-.',label='S22')    # Plot some data on the axes.
ax3.axhline(y=25, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax3.axhline(y=62.5, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax3.axhline(y=125, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax3.axhline(y=275, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 


ax3.set_xlabel('Vertical Stress (MPa)',fontsize=10, fontweight='bold')  # Add an x-label to the axes.
ax3.set_ylabel('Depth (mm)',fontsize=10, fontweight='bold')  # Add a y-label to the axes.
ax3.set_title("Vertical Stress AC",fontsize=10, fontweight='bold')  # Add a title to the axes.
ax3.legend(bbox_to_anchor=(0.05, 0.05, 0.3, 4), loc='lower left',
                      ncol=1, mode="expand", borderaxespad=0.)
ax3.legend(fontsize=9)

ax3.set_xlim(0,-0.8)
ax3.set_ylim(0,750)
ax3.minorticks_on()
ax3.xaxis.grid(True, which='minor')
ax3.yaxis.grid(True, which='minor')
ax3.invert_xaxis()
ax3.invert_yaxis()

ax3.text(-0.475,625, 'S22 Max,AC=-0.69',fontsize=9, style='italic', 
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})
ax3.text(-0.475,705, 'S22 Min,AC=-0.00', fontsize=9, style='italic',
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})

plt.subplots_adjust(bottom=0.1, right=1.5, top=0.8)


#%%
#[FIGURE 4 ]================================
ax4.plot(Y,X,'b',label='S22')    # Plot some data on the axes.
ax4.plot(Y,X,'g-.',label='S22')    # Plot some data on the axes.
ax4.axhline(y=25, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax4.axhline(y=62.5, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax4.axhline(y=125, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax4.axhline(y=275, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 


ax4.set_xlabel('Vertical Stress (MPa)',fontsize=10, fontweight='bold')  # Add an x-label to the axes.
ax4.set_ylabel('Depth (mm)',fontsize=10, fontweight='bold')  # Add a y-label to the axes.
ax4.set_title("Vertical Stress AC",fontsize=10, fontweight='bold')  # Add a title to the axes.
ax4.legend(bbox_to_anchor=(0.05, 0.05, 0.3, 4), loc='lower left',
                      ncol=1, mode="expand", borderaxespad=0.)
ax4.legend(fontsize=9)

ax4.set_xlim(0,-0.8)
ax4.set_ylim(0,750)
ax4.minorticks_on()
ax4.xaxis.grid(True, which='minor')
ax4.yaxis.grid(True, which='minor')
ax4.invert_xaxis()
ax4.invert_yaxis()

ax4.text(-0.475,625, 'S22 Max,AC=-0.69',fontsize=9, style='italic', 
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})
ax4.text(-0.475,705, 'S22 Min,AC=-0.00', fontsize=9, style='italic',
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})

plt.subplots_adjust(bottom=0.1, right=1.5, top=0.8)


#%%
#[FIGURE 5 ]================================
ax5.plot(Y,X,'b',label='S22')    # Plot some data on the axes.
ax5.plot(Y,X,'g-.',label='S22')    # Plot some data on the axes.
ax5.axhline(y=25, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax5.axhline(y=62.5, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax5.axhline(y=125, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax5.axhline(y=275, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 


ax5.set_xlabel('Vertical Stress (MPa)',fontsize=10, fontweight='bold')  # Add an x-label to the axes.
ax5.set_ylabel('Depth (mm)',fontsize=10, fontweight='bold')  # Add a y-label to the axes.
ax5.set_title("Vertical Stress AC",fontsize=10, fontweight='bold')  # Add a title to the axes.
ax5.legend(bbox_to_anchor=(0.05, 0.05, 0.3, 4), loc='lower left',
                      ncol=1, mode="expand", borderaxespad=0.)
ax5.legend(fontsize=9)

ax5.set_xlim(0,-0.8)
ax5.set_ylim(0,750)
ax5.minorticks_on()
ax5.xaxis.grid(True, which='minor')
ax5.yaxis.grid(True, which='minor')
ax5.invert_xaxis()
ax5.invert_yaxis()

ax5.text(-0.475,625, 'S22 Max,AC=-0.69',fontsize=9, style='italic', 
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})
ax5.text(-0.475,705, 'S22 Min,AC=-0.00', fontsize=9, style='italic',
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})

plt.subplots_adjust(bottom=0.1, right=1.5, top=0.8)


#%%
#[FIGURE 6 ]================================
ax6.plot(Y,X,'b',label='S22')    # Plot some data on the axes.
ax6.plot(Y,X,'g-.',label='S22')    # Plot some data on the axes.
ax6.axhline(y=25, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax6.axhline(y=62.5, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax6.axhline(y=125, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax6.axhline(y=275, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 


ax6.set_xlabel('Vertical Stress (MPa)',fontsize=10, fontweight='bold')  # Add an x-label to the axes.
ax6.set_ylabel('Depth (mm)',fontsize=10, fontweight='bold')  # Add a y-label to the axes.
ax6.set_title("Vertical Stress AC",fontsize=10, fontweight='bold')  # Add a title to the axes.
ax6.legend(bbox_to_anchor=(0.05, 0.05, 0.3, 4), loc='lower left',
                      ncol=1, mode="expand", borderaxespad=0.)
ax6.legend(fontsize=9)

ax6.set_xlim(0,-0.8)
ax6.set_ylim(0,750)
ax6.minorticks_on()
ax6.xaxis.grid(True, which='minor')
ax6.yaxis.grid(True, which='minor')
ax6.invert_xaxis()
ax6.invert_yaxis()

ax6.text(-0.475,625, 'S22 Max,AC=-0.69',fontsize=9, style='italic', 
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})
ax6.text(-0.475,705, 'S22 Min,AC=-0.00', fontsize=9, style='italic',
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})

plt.subplots_adjust(bottom=0.1, right=1.5, top=0.8)


#%%
#[FIGURE 7 ]================================
ax7.plot(Y,X,'b',label='S22')    # Plot some data on the axes.
ax7.plot(Y,X,'g-.',label='S22')    # Plot some data on the axes.
ax7.axhline(y=25, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax7.axhline(y=62.5, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax7.axhline(y=125, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax7.axhline(y=275, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 


ax7.set_xlabel('Vertical Stress (MPa)',fontsize=10, fontweight='bold')  # Add an x-label to the axes.
ax7.set_ylabel('Depth (mm)',fontsize=10, fontweight='bold')  # Add a y-label to the axes.
ax7.set_title("Vertical Stress AC",fontsize=10, fontweight='bold')  # Add a title to the axes.
ax7.legend(bbox_to_anchor=(0.05, 0.05, 0.3, 4), loc='lower left',
                      ncol=1, mode="expand", borderaxespad=0.)
ax7.legend(fontsize=9)

ax7.set_xlim(0,-0.8)
ax7.set_ylim(0,750)
ax7.minorticks_on()
ax7.xaxis.grid(True, which='minor')
ax7.yaxis.grid(True, which='minor')
ax7.invert_xaxis()
ax7.invert_yaxis()

ax7.text(-0.475,625, 'S22 Max,AC=-0.69',fontsize=9, style='italic', 
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})
ax7.text(-0.475,705, 'S22 Min,AC=-0.00', fontsize=9, style='italic',
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})

plt.subplots_adjust(bottom=0.1, right=1.5, top=0.8)


#%%
#[FIGURE 8 ]================================
ax8.plot(Y,X,'b',label='S22')    # Plot some data on the axes.
ax8.plot(Y,X,'g-.',label='S22')    # Plot some data on the axes.
ax8.axhline(y=25, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax8.axhline(y=62.5, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax8.axhline(y=125, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax8.axhline(y=275, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 


ax8.set_xlabel('Vertical Stress (MPa)',fontsize=10, fontweight='bold')  # Add an x-label to the axes.
ax8.set_ylabel('Depth (mm)',fontsize=10, fontweight='bold')  # Add a y-label to the axes.
ax8.set_title("Vertical Stress AC",fontsize=10, fontweight='bold')  # Add a title to the axes.
ax8.legend(bbox_to_anchor=(0.05, 0.05, 0.3, 4), loc='lower left',
                      ncol=1, mode="expand", borderaxespad=0.)
ax8.legend(fontsize=9)

ax8.set_xlim(0,-0.8)
ax8.set_ylim(0,750)
ax8.minorticks_on()
ax8.xaxis.grid(True, which='minor')
ax8.yaxis.grid(True, which='minor')
ax8.invert_xaxis()
ax8.invert_yaxis()

ax8.text(-0.475,625, 'S22 Max,AC=-0.69',fontsize=9, style='italic', 
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})
ax8.text(-0.475,705, 'S22 Min,AC=-0.00', fontsize=9, style='italic',
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})

plt.subplots_adjust(bottom=0.1, right=1.5, top=0.8)


#%%
#[FIGURE 9 ]================================
ax9.plot(Y,X,'b',label='S22')    # Plot some data on the axes.
ax9.plot(Y,X,'g-.',label='S22')    # Plot some data on the axes.
ax9.axhline(y=25, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax9.axhline(y=62.5, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax9.axhline(y=125, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 
ax9.axhline(y=275, color='r', linestyle='-.',linewidth=0.25) #Plot Horizontal Line 


ax9.set_xlabel('Vertical Stress (MPa)',fontsize=10, fontweight='bold')  # Add an x-label to the axes.
ax9.set_ylabel('Depth (mm)',fontsize=10, fontweight='bold')  # Add a y-label to the axes.
ax9.set_title("Vertical Stress AC",fontsize=10, fontweight='bold')  # Add a title to the axes.
ax9.legend(bbox_to_anchor=(0.05, 0.05, 0.3, 4), loc='lower left',
                      ncol=1, mode="expand", borderaxespad=0.)
ax2.legend(fontsize=9)

ax9.set_xlim(0,-0.8)
ax9.set_ylim(0,750)
ax9.minorticks_on()
ax9.xaxis.grid(True, which='minor')
ax9.yaxis.grid(True, which='minor')
ax9.invert_xaxis()
ax9.invert_yaxis()

ax9.text(-0.475,625, 'S22 Max,AC=-0.69',fontsize=9, style='italic', 
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})
ax9.text(-0.475,705, 'S22 Min,AC=-0.00', fontsize=9, style='italic',
        bbox={'facecolor': 'white', 'alpha': 0.4, 'pad': 4})

plt.subplots_adjust(bottom=0.1, right=1.5, top=0.8)
