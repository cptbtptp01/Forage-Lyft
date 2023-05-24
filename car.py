from abc import ABC, abstractmethod

from engine import Engine
from battery import Battery


class Car(ABC):
    def __init__(self, engine, battery) -> None:
        
        self.engine = engine
        self.battery = battery
    
    @abstractmethod
    def battery_needs_service(self) -> bool:
        pass
    
    @abstractmethod
    def engine_needs_service(self) -> bool:
        pass
    
    def need_service(self) -> bool:
        return self.battery.battery_needs_service() or self.engine.engine_needs_service()