"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number

FakeA = MonitoringStation("fakea", "fakemeasurea", "A", (0, 10), (-1, 100), "River A", "Town A")

FakeB = MonitoringStation("fakeb", "fakemeasureb", "B", (0, 100), None, "River B", "Town B")

FakeC = MonitoringStation("fakec", "fakemeasurec", "C", (0, 180), (100, -1), "River C", "Town C")

FakeList = [FakeA, FakeB, FakeC]

def test_stations_by_distance():
    
    a = stations_by_distance(FakeList, (0, 0))
    
    assert a[0][0] == FakeA
    assert a[1][0] == FakeB
    assert a[2][0] == FakeC
    
def test_stations_within_radius():

    a = stations_within_radius(FakeList, (0, 0), 2000)
    
    assert a == [FakeA]
    
def test_rivers_with_station():
    
    a = rivers_with_station(FakeList)
    
    assert a == set(["River A", "River B", "River C"])

def test_stations_by_river():
    
    a = stations_by_river(FakeList)
    
    assert a["River A"] == [FakeA]

def test_rivers_by_station_number():
    
    a = rivers_by_station_number(FakeList, 1)
    
    assert ('River A', 1) in a
    assert ('River B', 1) in a
    assert ('River C', 1) in a
    