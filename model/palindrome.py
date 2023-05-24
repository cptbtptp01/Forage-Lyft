from datetime import datetime

from car import Car
from engines.sternman_engine import SternmanEngine
from batteries.spindler_battery import SpindlerBattery


class Palindrome(Car):
    def __init__(self, engine, battery, warning_lights_on, last_service_date) -> None:
        super().__init__(engine, battery)
        self.engine = SternmanEngine(warning_lights_on)
        self.battery = SpindlerBattery(last_service_date)

    def needs_service(self):
        return self.battery.battery_needs_service() or self.engine.engine_needs_service()
