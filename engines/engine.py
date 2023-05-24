from abc import ABC, abstractclassmethod

class Engine(ABC):
    
    @abstractclassmethod
    def need_service(self):
        pass