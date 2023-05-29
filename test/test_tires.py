# ensure that the parent directory is on the path
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import unittest

from tires.carrigan_tire import CarriganTire
from tires.octoprime_tire import OctoprimeTire

class TestCarrigan(unittest.TestCase):
    def setUp(self) -> None:
        self.tire_sensors_ok = [0,0,0,0]
        self.tire_sensors_not_ok = [1,0,0,0]
        self.tires = CarriganTire(None)
    
    def test_need_service(self):
        self.tires.sensors = self.tire_sensors_not_ok
        self.assertTrue(self.tires.need_service())
    
    def test_not_need_service(self):
        self.tires.sensors = self.tire_sensors_ok
        self.assertFalse(self.tires.need_service())

class TestOctoprime(unittest.TestCase):
    def setUp(self) -> None:
        self.tire_sensors_ok = [0,0,0,0]
        self.tire_sensors_not_ok = [1,1,1,0]
        self.tires = OctoprimeTire(None)
    
    def test_need_service(self):
        self.tires.sensors = self.tire_sensors_not_ok
        self.assertTrue(self.tires.need_service())
    
    def test_not_need_service(self):
        self.tires.sensors = self.tire_sensors_ok
        self.assertFalse(self.tires.need_service())

if __name__ == '__main__':
    # or run in command line: python -m unittest test.test_tires
    unittest.main()