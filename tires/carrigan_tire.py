from tires.tire import Tire
from utils.utils import check_values_in_array

# sensors = [_,_,_,_] 4 numbers between 0 - 1, inclusive, representing how worn each of the tires are
# passed in the carFactory, and use in the tire classes

class CarriganTire(Tire):
    def __init__(self, sensors:list) -> None:
        self.sensors = sensors
    def need_service(self) -> bool:
        return check_values_in_array(self.sensors, 0.9)