from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river
from floodsystem.utils import sorted_by_key

def run():
    """Task 1D"""
    
    stations = build_station_list()
    a = rivers_with_station(stations)
    print(str(len(a)) + " stations. First 10 - " + str(sorted(list(a))[0:10]), sep="")
    river_names = ["River Aire", "River Cam", "River Thames"]
    dic = stations_by_river(stations)
    
    good_station_name = []
    
    for river_name in river_names:
        for good_station in dic[river_name]:
            good_station_name.append(good_station.name)
        print(sorted(good_station_name))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
