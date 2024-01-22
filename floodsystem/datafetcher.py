# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides functionality for retrieving real-time and
latest time history level data

"""

import datetime
import json
import os

import dateutil.parser
import requests


def fetch(url):
    """Fetch data from url and return fetched JSON object"""
    r = requests.get(url)
    data = r.json()
    return data


def dump(data, filename):
    """Save JSON object to file"""
    f = open(filename, 'w')
    data = json.dump(data, f)
    f.close()


def load(filename):
    """Load JSON object from file"""
    f = open(filename, 'r')
    data = json.load(f)
    f.close()
    return data


def fetch_station_data(use_cache=True):
    """Fetch data from Environment agency for all active river level
    monitoring stations via a REST API and return retrieved data as a
    JSON object.

    Fetched data is dumped to a cache file so on subsequent call it can
    optionally be retrieved from the cache file. This is faster than
    retrieval over the Internet and avoids excessive calls to the
    Environment Agency service.

    """

    # URL for retrieving data for active stations with river level
    # monitoring (see
    # http://environment.data.gov.uk/flood-monitoring/doc/reference)
    url = "http://environment.data.gov.uk/flood-monitoring/id/stations?status=Active&parameter=level&qualifier=Stage&_view=full"  # noqa

    sub_dir = 'cache'
    try:
        os.makedirs(sub_dir)
    except FileExistsError:
        pass
    cache_file = os.path.join(sub_dir, 'station_data.json')

    # Implemented by bc604: Record/Read data update datetime to determine whether to update cache.
    lines = None
    try:
        with open(os.path.join(sub_dir, 'station_data_last_update.txt'), 'r') as f:
            lines = f.readlines()
    except FileNotFoundError: # no latest update date, so don't use cache.
        use_cache = False

    if use_cache:
        lines = lines[0]
        if '\n' in lines:
            lines = lines[0:-1] # removes the \n at the end
        update_datetime = datetime.datetime.strptime(lines, '%y-%m-%d %H:%M:%S')
        if update_datetime + datetime.timedelta(seconds=3600) < datetime.datetime.now():
            # More than 1h old
            use_cache = False

    # Attempt to load station data from file, otherwise fetch over
    # Internet
    if use_cache:
        try:
            # Attempt to load from file
            data = load(cache_file)
        except FileNotFoundError:
            # If load from file fails, fetch and dump to file
            data = fetch(url)
            dump(data, cache_file)
            with open(os.path.join(sub_dir, 'station_data_last_update.txt'), 'w') as f:
                f.writelines(datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))
    else:
        # Fetch and dump to file
        data = fetch(url)
        dump(data, cache_file)
        with open(os.path.join(sub_dir, 'station_data_last_update.txt'), 'w') as f:
            f.writelines(datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))

    return data


def fetch_latest_water_level_data(use_cache=True):
    """Fetch latest levels from all 'measures'. Returns JSON object"""

    # URL for retrieving data
    url = "http://environment.data.gov.uk/flood-monitoring/id/measures?parameter=level&qualifier=Stage&qualifier=level"  # noqa

    sub_dir = 'cache'
    try:
        os.makedirs(sub_dir)
    except FileExistsError:
        pass
    cache_file = os.path.join(sub_dir, 'level_data.json')

    # Implemented by bc604: Record/Read data update datetime to determine whether to update cache.
    lines = None
    try:
        with open(os.path.join(sub_dir, 'level_data_last_update.txt'), 'r') as f:
            lines = f.readlines()
    except FileNotFoundError: # no latest update date, so don't use cache.
        use_cache = False

    if use_cache:
        lines = lines[0]
        if '\n' in lines:
            lines = lines[0:-1] # removes the \n at the end
        update_datetime = datetime.datetime.strptime(lines, '%y-%m-%d %H:%M:%S')
        if update_datetime + datetime.timedelta(seconds=3600) < datetime.datetime.now():
            # More than 1h old
            use_cache = False

    # Attempt to load level data from file, otherwise fetch over
    # Internet
    if use_cache:
        try:
            # Attempt to load from file
            data = load(cache_file)
        except FileNotFoundError:
            data = fetch(url)
            dump(data, cache_file)
            with open(os.path.join(sub_dir, 'level_data_last_update.txt'), 'w') as f:
                f.writelines(datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))
    else:
        data = fetch(url)
        dump(data, cache_file)
        with open(os.path.join(sub_dir, 'level_data_last_update.txt'), 'w') as f:
            f.writelines(datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))

    return data


def fetch_measure_levels(measure_id, dt):
    """
    Fetch measure levels from latest reading and going back a period
    dt. Return list of dates and a list of values.
    """

    # Current time (UTC)
    #now = datetime.datetime.utcnow()
    now = datetime.datetime.now()

    # Start time for data
    start = now - dt

    # Construct URL for fetching data
    url_base = measure_id
    url_options = "/readings/?_sorted&since=" + start.isoformat() + 'Z'
    url = url_base + url_options

    # Fetch data
    data = fetch(url)

    # Extract dates and levels
    dates, levels = [], []
    for measure in data['items']:
        # Convert date-time string to a datetime object
        d = dateutil.parser.parse(measure['dateTime'])

        # Append data
        try:
            levels.append(measure['value'])
        except KeyError:
            continue
        dates.append(d)

    return dates, levels

def fetch_official_flood(use_cache=True):
    
    """
    This is like cheating lol so not actually using it in Task 2G.
    Good to have the official flood data though.
    """
    
    url = "http://environment.data.gov.uk/flood-monitoring/id/floods?min-severity=3"
    
    sub_dir = 'cache'
    try:
        os.makedirs(sub_dir)
    except FileExistsError:
        pass
    cache_file = os.path.join(sub_dir, 'flood_data.json')
    
    lines = None
    try:
        with open(os.path.join(sub_dir, 'flood_data_last_update.txt'), 'r') as f:
            lines = f.readlines()
    except FileNotFoundError: # no latest update date, so don't use cache.
        use_cache = False

    if use_cache:
        lines = lines[0]
        if '\n' in lines:
            lines = lines[0:-1] # removes the \n at the end
        update_datetime = datetime.datetime.strptime(lines, '%y-%m-%d %H:%M:%S')
        if update_datetime + datetime.timedelta(seconds=3600) < datetime.datetime.now():
            # More than 1h old
            use_cache = False
    
    # Attempt to load level data from file, otherwise fetch over
    # Internet
    if use_cache:
        try:
            # Attempt to load from file
            data = load(cache_file)
        except FileNotFoundError:
            data = fetch(url)
            dump(data, cache_file)
            with open(os.path.join(sub_dir, 'flood_data_last_update.txt'), 'w') as f:
                f.writelines(datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))
    else:
        data = fetch(url)
        dump(data, cache_file)
        with open(os.path.join(sub_dir, 'flood_data_last_update.txt'), 'w') as f:
            f.writelines(datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))
            
    return data