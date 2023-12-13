from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Task 1E"""
    
    stations = build_station_list()
    a = rivers_by_station_number(stations, 9)
    print(a)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
