from floodsystem.analysis import polyfit, town_threat
from datetime import datetime

def test_polyfit():
    assert polyfit([0, 1, 2], [1, 2, 3], 3) == (0, 0)
    assert polyfit([datetime(2024, 1, 1, 0, 0, 0), datetime(2024, 1, 2, 0, 0, 0)], [1, 2, 3], 3) == (0, 0)
    assert polyfit([datetime(2024, 1, 1, 0, 0, 0)], [1, [1, 2], 3], 3) == (0, 0)
