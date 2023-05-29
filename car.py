from car_service import CarService


class Car(CarService):
    def __init__(self, engine, battery, tires) -> None:
        
        self.engine = engine
        self.battery = battery
        self.tires = tires
    
    def need_service(self) -> bool:
        return self.engine.need_service() or self.battery.need_service() or self.tires.need_service()