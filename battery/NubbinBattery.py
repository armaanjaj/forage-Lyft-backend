from Battery import Battery
from datetime import date
from utils import add_years_to_date

class NubbinBattery(Battery):

    def __init__(self, last_service_date:date, current_date:date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 4)

        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False