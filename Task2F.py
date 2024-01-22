import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    highest = stations_highest_rel_level(stations, 5)
    dt=2
    #print(highest)
    datess = []
    levelss = []
    stationss = []
    for (station, data) in highest:
        #print(station)
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        datess.append(dates)
        levelss.append(levels)
        stationss.append(station)
    plot_water_level_with_fit(stationss, datess, levelss, 4)
    
if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
