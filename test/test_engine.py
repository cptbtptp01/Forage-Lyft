import unittest
from datetime import datetime

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine

class TestCapulet(unittest.TestCase):
    def setUp(self) -> None:
        self.current_mileage_not_exceed = 30000
        self.current_mileage_exceed = 30001
        self.engine = CapuletEngine(current_mileage=None,last_service_mileage=0)

    def test_need_servive(self):
        self.engine.current_mileage = self.current_mileage_exceed
        self.assertTrue(self.engine.need_service())

    def test_not_need_servive(self):
        self.engine.current_mileage = self.current_mileage_not_exceed
        self.assertFalse(self.engine.need_service())

class TestWilloughby(unittest.TestCase):
    def setUp(self) -> None:
        self.current_mileage_not_exceed = 60000
        self.current_mileage_exceed = 60001
        self.engine = WilloughbyEngine(current_mileage=None,last_service_mileage=0)

    def test_need_servive(self):
        self.engine.current_mileage = self.current_mileage_exceed
        self.assertTrue(self.engine.need_service())

    def test_not_need_servive(self):
        self.engine.current_mileage = self.current_mileage_not_exceed
        self.assertFalse(self.engine.need_service())

class TestSternman(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = SternmanEngine(warning_light_on=False)

    def test_need_sevice(self):
        self.engine.warning_light_on = True
        self.assertTrue(self.engine.need_service())
    
    def test_need_sevice(self):
        self.assertFalse(self.engine.need_service())