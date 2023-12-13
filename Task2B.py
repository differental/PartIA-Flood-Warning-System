from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    """Task 2B"""
    
    stations = build_station_list()
    update_water_levels(stations)
    a = stations_level_over_threshold(stations, 0.8)
    for item in a:
        print(item[0].name, item[1], sep=" ", end="\n")

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
