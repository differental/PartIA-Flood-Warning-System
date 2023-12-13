from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Task 1C"""

    stations = build_station_list()
    a = stations_within_radius(stations, (52.2053, 0.1218), 10)
    b = []
    for item in a:
        b.append(item.name)
    b.sort()
    print(b)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
