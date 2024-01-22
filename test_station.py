# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations

FakeA = MonitoringStation("fakea", "fakemeasurea", "A", (0, 10), (-1, 100), "River A", "Town A")

FakeB = MonitoringStation("fakeb", "fakemeasureb", "B", (0, 100), None, "River B", "Town B")

FakeC = MonitoringStation("fakec", "fakemeasurec", "C", (0, 180), (100, -1), "River C", "Town C")

FakeList = [FakeA, FakeB, FakeC]

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():
    
    a = inconsistent_typical_range_stations(FakeList)
    
    assert FakeB in a
    assert FakeC in a
    assert len(a) == 2