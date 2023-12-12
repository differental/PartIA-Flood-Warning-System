# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import Unit, haversine

from .station import MonitoringStation
from .utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    """This function calculates the distance between a list of
    stations and a given coordinate p, sorts them based on the
    distance between each station and p, and outputs a sorted
    list of stations and their distance to p.

    """
    output = []
    for station in stations:
        output.append((station, haversine(station.coord, p)))
    output = sorted_by_key(output, 1)
    return output


def stations_within_radius(stations, centre, r):
    """This function calculates the distance between a list of
    stations and filters out the ones that are further than "r"
    from the centre coordinates "centre". Outputs a list of
    stations after the distance filtering.

    """
    output = []
    for station in stations:
        if haversine(station.coord, centre) <= r:
            output.append(station)
    return output
