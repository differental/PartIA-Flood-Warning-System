# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    output = []
    for station in stations:
        output.append((station, haversine(station.coord, p)))
    output = sorted_by_key(output, 1)
    return output
