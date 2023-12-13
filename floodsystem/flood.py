"""
This module provides flood related stuff. Update this afterwards.
"""

from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    output = []
    for station in stations:
        if (not station.relative_water_level() == None) and station.relative_water_level() > tol:
            output.append((station, station.relative_water_level()))
    return sorted_by_key(output, 1, True)

