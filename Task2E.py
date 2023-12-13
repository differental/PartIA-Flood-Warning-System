import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    highest = stations_highest_rel_level(stations, 5)
    dt=10
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
    plot_water_levels(stationss, datess, levelss)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
