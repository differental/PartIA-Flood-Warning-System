# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

"""
This module contains a collection of functions related to
geographical data.
"""

from haversine import haversine
from .utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    """
    This function calculates the distance between a list of
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
    """
    This function calculates the distance between a list of
    stations and filters out the ones that are further than "r"
    from the centre coordinates "centre". Outputs a list of
    stations after the distance filtering.
    """

    output = []
    for station in stations:
        if haversine(station.coord, centre) <= r:
            output.append(station)
    return output


def rivers_with_station(stations):
    """
    This function returns a set of rivers that have stations
    monitoring them.
    """

    output = set([])
    for station in stations:
        output.add(station.river)
    return output


def stations_by_river(stations):
    """
    This function returns a dictionary that maps river names
    to a list of station objects on that river.
    """

    output = {}
    for station in stations:
        if station.river not in output.keys():
            output[station.river] = []
        output[station.river].append(station)
    return output


def rivers_by_station_number(stations, N):
    """
    This function returns the N rivers with the most number
    of stations.
    """

    rivers = rivers_with_station(stations)
    dic = stations_by_river(stations)
    results = []
    for river in rivers:
        results.append((river, len(dic[river])))
    results = sorted_by_key(results, 1, True)

    output = []
    for i in range(N):
        output.append(results[i])
    for i in range(N, len(results)):
        if results[i][1] < results[N - 1][1]:
            break
        output.append(results[i])
    return output

