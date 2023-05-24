from abc import ABC, abstractmethod


class CarService(ABC):
    @abstractmethod
    def need_service(self):
        pass