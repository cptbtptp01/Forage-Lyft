from abc import ABC, abstractclassmethod

class Tire(ABC):
    
    @abstractclassmethod
    def need_service(self):
        pass