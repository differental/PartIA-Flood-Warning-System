from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Task 1F"""
    
    stations = build_station_list()
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    names = []
    for station in inconsistent_stations:
        names.append(station.name)
    print(sorted(names))

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
