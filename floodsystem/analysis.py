"""
Analysis stuff, done by Mihnea
"""

import numpy as np
from matplotlib.dates import date2num

def polyfit(dates, levels, p):
    
    datesnew = np.array(date2num(dates))
    p_coeff = np.polyfit(datesnew - datesnew[0], levels, p)
    poly = np.poly1d(p_coeff)
    
    return poly, datesnew[0]