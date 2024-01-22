"""
This module does some plotting.
"""

from .analysis import polyfit
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import numpy as np

def plot_water_levels(stations, dates, levels):
    
    if not len(stations) == len(dates) == len(levels):
        raise IndexError
    
    fig, ax = plt.subplots(nrows=3, ncols=2)
    for i in range(len(stations)):
        ax[i%3, i//3].plot(dates[i], levels[i], label = "Actual Data")
        ax[i%3, i//3].plot(dates[i], [stations[i].typical_range[0] for j in range(len(dates[i]))], label = "Min Typical")
        ax[i%3, i//3].plot(dates[i], [stations[i].typical_range[1] for j in range(len(dates[i]))], label = "Max Typical")
        #ax[i%3, i//3].xlabel('Date')
        #ax[i%3, i//3].ylabel('Water Level (m)')
        #ax[i%3, i//3].xticks(rotation=45)
        ax[i%3, i//3].tick_params(labelrotation=45)
        ax[i%3, i//3].set_title(stations[i].name)
        ax[i%3, i//3].legend()
        #ax[i%3, i//3].tight_layout()
    fig.supxlabel('Date')
    fig.supylabel('Water Level (m)')
    fig.suptitle('Water Levels for ' + str(len(stations)) + ' stations')
    plt.show()
    return

def plot_water_level_with_fit(stations, dates, levels, p):
    
    if not len(stations) == len(dates) == len(levels):
        raise IndexError
    
    fig, ax = plt.subplots(nrows=3, ncols=2)
    for i in range(len(stations)):
        ax[i%3, i//3].plot(dates[i], levels[i], label = "Actual Data")
        ax[i%3, i//3].plot(dates[i], [stations[i].typical_range[0] for j in range(len(dates[i]))], label = "Min Typical")
        ax[i%3, i//3].plot(dates[i], [stations[i].typical_range[1] for j in range(len(dates[i]))], label = "Max Typical")
        if len(dates[i]):
            poly, d0 = polyfit(dates[i], levels[i], p)
            if d0 == 0:
                continue
            ax[i%3, i//3].plot(dates[i], poly(np.array(date2num(dates[i])) - d0), label = "Polyfit")
        
        #ax[i%3, i//3].xlabel('Date')
        #ax[i%3, i//3].ylabel('Water Level (m)')
        #ax[i%3, i//3].xticks(rotation=45)
        ax[i%3, i//3].tick_params(labelrotation=45)
        ax[i%3, i//3].set_title(stations[i].name)
        ax[i%3, i//3].legend()
        #ax[i%3, i//3].tight_layout()
    fig.supxlabel('Date')
    fig.supylabel('Water Level (m)')
    fig.suptitle('Water Levels for ' + str(len(stations)) + ' stations')
    plt.show()
    return
