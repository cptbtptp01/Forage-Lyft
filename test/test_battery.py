import unittest
from datetime import datetime

from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

class TestNubbin(unittest.TestCase):
    def setUp(self) -> None:
        self.current_date = datetime.today().date()
        self.nubbin_last_service_not_expire = self.current_date.replace(year=self.current_date.year-4)
        self.nubbin_last_service_expire = self.current_date.replace(year=self.current_date.year-4, day=self.current_date.day-1)
        self.battery = NubbinBattery(self.current_date, last_service_date=None)
    
    def test_need_service(self):
        self.battery.last_service_date = self.nubbin_last_service_expire
        self.assertTrue(self.battery.need_service())
    
    def test_not_need_service(self):
        self.battery.last_service_date = self.nubbin_last_service_not_expire
        self.assertFalse(self.battery.need_service())

class TestSpindler(unittest.TestCase):
    def setUp(self) -> None:
        self.current_date = datetime.today().date()
        self.spinder_last_service_not_expire = self.current_date.replace(year=self.current_date.year-2)
        self.spinder_last_service_expire = self.current_date.replace(year=self.current_date.year-2, day=self.current_date.day-1)
        self.battery = SpindlerBattery(self.current_date, last_service_date=None)

    def test_need_service(self):
        self.battery.last_service_date = self.spinder_last_service_expire
        self.assertTrue(self.battery.need_service())

    def test_not_need_service(self):
        self.battery.last_service_date = self.spinder_last_service_not_expire
        self.assertFalse(self.battery.need_service())