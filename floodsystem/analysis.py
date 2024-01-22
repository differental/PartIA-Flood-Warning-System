"""
Analysis stuff, done by Mihnea
"""

from .datafetcher import fetch_measure_levels
from .flood import stations_level_over_threshold
from .utils import sorted_by_key

import numpy as np
import datetime
from matplotlib.dates import date2num

class UnRealisticError (Exception):
    pass

def polyfit(dates, levels, p):
    
    datesnew = np.array(date2num(dates))
    
    if not all(isinstance(n, (int, float)) for n in datesnew):
        return 0, 0
    
    if not all(isinstance(n, (int, float)) for n in levels):
        return 0, 0
    
    p_coeff = np.polyfit(datesnew - np.min(datesnew), levels, p)
    poly = np.poly1d(p_coeff)
    
    return poly, np.min(datesnew)

def town_threat(stations, tol=1.1, trackdate=10, futuredate=2):

    futuredatetimes = np.linspace(date2num(datetime.datetime.now()), date2num(datetime.datetime.now()) + futuredate, 10)
    
    dangerous = stations_level_over_threshold(stations, tol)
    
    results = {}
    
    print(len(dangerous))
    count = 0
    
    for (station, data) in dangerous:
        
        if not station.typical_range_consistent:
            continue
        
        if station.town == None:
            continue
        
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=trackdate))

        count += 1
        print("Measure levels fetched for " + station.name + ". Num: " + str(count))
        
        if len(dates) > 0:
            poly, d0 = polyfit(dates, levels, 4)
            if d0 == 0: #Unable to polyfit due to corrupted data
                continue
            predicted = poly(futuredatetimes - d0)
            if ((np.max(predicted) - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0]) > 100):
                # When the predicted results are larger than 100
                # Then either an entire town will die, or the polyfit
                # was not a good approximation
                raise UnRealisticError("Predicted Number Too Large")
                #print(poly, np.max(predicted), d0)
                #plt.plot(dates, levels, label = "Actual Data")
                #plt.plot(dates, poly(np.array(date2num(dates)) - d0), label = "Polyfit")
                #plt.plot(futuredatetimes, predicted)
                #plt.show()
        
            results[station.town] = max(results.get(station.town, 0), (np.max(predicted) - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0]))
    
    results = sorted_by_key(((town, val) for town, val in results.items()), 1, True)
    
    flag=False
    for i in range(len(results)):
        if results[i][1] < tol:
            flag=True
            break
    if flag:
        results = results[0:i]
    
    return results