from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    """Task 2C"""
    
    stations = build_station_list()
    update_water_levels(stations)
    a = stations_highest_rel_level(stations, 10)
    for item in a:
        print(item[0].name, item[1], sep=" ", end="\n")

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
