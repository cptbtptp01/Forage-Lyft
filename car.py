from car_service import CarService


class Car(CarService):
    def __init__(self, engine, battery) -> None:
        
        self.engine = engine
        self.battery = battery
    
    def need_service(self) -> bool:
        return self.engine.need_service() or self.battery.need_service()