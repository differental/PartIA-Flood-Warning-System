import unittest
from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit

FakeA = MonitoringStation("fakea", "fakemeasurea", "A", (0, 10), (-1, 100), "River A", "Town A")

FakeList = [FakeA]

class TestCase(unittest.TestCase):
    def test_plot_water_levels(self):
        self.assertRaises(IndexError, plot_water_levels, FakeList, [1, 2], [2])
        self.assertRaises(IndexError, plot_water_levels, FakeList, [1], [2, 3])
        
    def test_plot_water_level_with_fit(self):
        self.assertRaises(IndexError, plot_water_level_with_fit, FakeList, [1, 2], [2], 3)
        self.assertRaises(IndexError, plot_water_level_with_fit, FakeList, [1], [2, 3], 3)
