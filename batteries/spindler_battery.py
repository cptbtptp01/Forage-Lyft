from utils.utils import add_years_to_date

from batteries.battery import Battery

class SpindlerBattery(Battery):
    
    def __init__(self, current_date, last_service_date) -> None:
        self.current_date = current_date
        self.last_service_date = last_service_date
    
    def need_service(self) -> bool:
        service_threshold_date = add_years_to_date(self.last_service_date, 2)
        
        return service_threshold_date < self.current_date