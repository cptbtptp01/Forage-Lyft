from tires.tire import Tire
from utils.utils import check_sums_in_array

class OctoprimeTire(Tire):
    def __init__(self, sensors:list) -> None:
        self.sensors = sensors
    def need_service(self) -> bool:
        return check_sums_in_array(self.sensors, 3)