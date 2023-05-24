from abc import ABC, abstractclassmethod

class Battery(ABC):
    
    @abstractclassmethod
    def need_service(self):
        pass