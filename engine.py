from abc import ABC, abstractclassmethod

class Engine(ABC):
    
    def __init__(self, current_mileage: int, last_service_mileage:int, warning_light_on=False) -> None:
        
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_on = warning_light_on 
    
    @abstractclassmethod
    def engine_needs_service(self):
        pass