from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.station import MonitoringStation

FakeA = MonitoringStation("fakea", "fakemeasurea", "A", (0, 0), (0.0, 1.0), "River A", "Town A")

FakeB = MonitoringStation("fakeb", "fakemeasureb", "B", (0, 0), None, "River B", "Town B")

FakeC = MonitoringStation("fakec", "fakemeasurec", "C", (0, 0), (1.0, 0.0), "River C", "Town C")

FakeD = MonitoringStation("faked", "fakemeasured", "D", (0, 0), (1.0, 11.0), "River B", "Town B")

FakeA.latest_level = 1.0
FakeC.latest_level = -10.0
FakeD.latest_level = 0.0

FakeList = [FakeA, FakeB, FakeC, FakeD]

def test_stations_level_over_threshold():
    
    a = stations_level_over_threshold(FakeList, 0.8)
    assert a == [(FakeA, 1.0)]

def test_stations_highest_rel_level():
    
    a = stations_highest_rel_level(FakeList, 3)
    assert a == [(FakeA, 1.0), (FakeD, -0.1)]