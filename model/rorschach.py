from datetime import datetime

from car import Car
from engines.willoughby_engine import WilloughbyEngine
from batteries.nubbin_battery import NubbinBattery


class Rorschach(Car):
    def __init__(self, engine:WilloughbyEngine, battery:NubbinBattery, current_mileage: int, last_service_mileage: int, last_service_date:datetime) -> None:
        super().__init__(engine, battery)
        self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.battery = NubbinBattery(last_service_date)

    def needs_service(self):
        return super().need_service()
