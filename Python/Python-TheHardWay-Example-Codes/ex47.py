from nose.tools import *
from ex47_test import Room

def test_room():
    gold = Room("GoldRoom")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.name, [])

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", )
