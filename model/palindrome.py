from datetime import datetime

from car import Car
from engines.sternman_engine import SternmanEngine
from batteries.spindler_battery import SpindlerBattery


class Palindrome(Car):
    def __init__(self, engine:SternmanEngine, battery:SpindlerBattery, current_mileage: int, last_service_mileage: int, last_service_date:datetime) -> None:
        super().__init__(engine, battery)
        self.engine = SternmanEngine(current_mileage, last_service_mileage)
        self.battery = SpindlerBattery(last_service_date)

    def needs_service(self):
        return super().need_service()
