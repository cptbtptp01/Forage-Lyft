from datetime import datetime

from car import Car
from engines.willoughby_engine import WilloughbyEngine
from batteries.nubbin_battery import NubbinBattery


class Rorschach(Car):
    def __init__(self, engine, battery, current_mileage, last_service_mileage, last_service_date) -> None:
        super().__init__(engine, battery)
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = NubbinBattery(last_service_date)

    def needs_service(self):
        return self.battery.battery_needs_service() or self.engine.engine_needs_service()
