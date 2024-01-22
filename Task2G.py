from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import town_threat

def run():
    
    stations = build_station_list()
    update_water_levels(stations)
    
    results = town_threat(stations, 1.1, 10, 2)
    output = []
    
    for (town, val) in results:
        level = "severe" if val >= 10 else "high" if val >= 5 else "moderate" if val >= 2 else "low"
        output.append((town, level))
    
    print(output)
    
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
