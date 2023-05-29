from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine

from tires.carrigan_tire import CarriganTire
from tires.octoprime_tire import OctoprimeTire

from car import Car

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensors) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTire(tire_sensors)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensors) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoprimeTire(tire_sensors)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light, tire_sensors) -> Car:
        engine = SternmanEngine(warning_light)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTire(tire_sensors)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensors) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTire(tire_sensors)
        car = Car(engine, battery, tires)
        return car
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_sensors) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTire(tire_sensors)
        car = Car(engine, battery, tires)
        return car