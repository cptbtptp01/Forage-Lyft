from abc import ABC, abstractclassmethod

class Battery(ABC):
    
    def __init__(self, last_service_date) -> None:
        
        self.last_service_date = last_service_date
    
    @abstractclassmethod
    def battery_needs_service(self):
        pass