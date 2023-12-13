from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Task 1B"""

    stations = build_station_list()
    a = stations_by_distance(stations, (52.2053, 0.1218))
    b = []
    for item in a:
        b.append((item[0].name, item[0].town, item[1]))
    print(b[:10], b[-10:], sep="\n\n\n")

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
