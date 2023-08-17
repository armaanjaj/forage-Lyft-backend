from datetime import date
from car import Car
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import SplinderBattery, NubbinBattery

class carFactory():

    def create_calliope(self, current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int) -> Car:
        return Car(
            battery = SplinderBattery(
                            current_date = current_date,
                            last_service_date = last_service_date
                        ),
            engine = CapuletEngine(
                            current_mileage = current_mileage,
                            last_service_mileage = last_service_mileage
                        )
        )

    def create_glissade(self, current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int) -> Car:
        return Car(
            battery = SplinderBattery(
                            current_date = current_date,
                            last_service_date = last_service_date
                        ),
            engine = WilloughbyEngine(
                            current_mileage = current_mileage,
                            last_service_mileage = last_service_mileage
                        )
        )

    def create_palindrome(self, current_date:date, last_service_date:date, warning_light_on: bool) -> Car:
        return Car(
            battery = SplinderBattery(
                            current_date = current_date,
                            last_service_date = last_service_date
                        ),
            engine = SternmanEngine(
                            warning_light_is_on = warning_light_on
                        )
        )

    def create_rorschach(self, current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int) -> Car:
        return Car(
            battery = NubbinBattery(
                            current_date = current_date,
                            last_service_date = last_service_date
                        ),
            engine = WilloughbyEngine(
                            current_mileage = current_mileage,
                            last_service_mileage = last_service_mileage
                        )
        )

    def create_thovex(self, current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int) -> Car:
        return Car(
            battery = NubbinBattery(
                            current_date = current_date,
                            last_service_date = last_service_date
                        ),
            engine = CapuletEngine(
                            current_mileage = current_mileage,
                            last_service_mileage = last_service_mileage
                        )
        )