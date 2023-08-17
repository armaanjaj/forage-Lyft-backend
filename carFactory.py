from datetime import date
from car import Car
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import SplinderBattery, NubbinBattery
from tire import CarriganTires, OctoprimeTires

class carFactory:

    @staticmethod
    def create_calliope(self, current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int, TireWearArray) -> Car:
        return Car(
            battery = SplinderBattery(
                            current_date = current_date,
                            last_service_date = last_service_date
                        ),
            engine = CapuletEngine(
                            current_mileage = current_mileage,
                            last_service_mileage = last_service_mileage
                        ),
            tire = CarriganTires(TireWearArray)
        )

    @staticmethod
    def create_glissade(self, current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int, TireWearArray) -> Car:
        return Car(
            battery = SplinderBattery(
                            current_date = current_date,
                            last_service_date = last_service_date
                        ),
            engine = WilloughbyEngine(
                            current_mileage = current_mileage,
                            last_service_mileage = last_service_mileage
                        ),
            tire = CarriganTires(TireWearArray)
        )

    @staticmethod
    def create_palindrome(self, current_date:date, last_service_date:date, warning_light_on: bool, TireWearArray) -> Car:
        return Car(
            battery = SplinderBattery(
                            current_date = current_date,
                            last_service_date = last_service_date
                        ),
            engine = SternmanEngine(
                            warning_light_is_on = warning_light_on
                        ),
            tire = CarriganTires(TireWearArray)
        )

    @staticmethod
    def create_rorschach(self, current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int, TireWearArray) -> Car:
        return Car(
            battery = NubbinBattery(
                            current_date = current_date,
                            last_service_date = last_service_date
                        ),
            engine = WilloughbyEngine(
                            current_mileage = current_mileage,
                            last_service_mileage = last_service_mileage
                        ),
            tire = OctoprimeTires(TireWearArray)
        )

    @staticmethod
    def create_thovex(self, current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int, TireWearArray) -> Car:
        return Car(
            battery = NubbinBattery(
                            current_date = current_date,
                            last_service_date = last_service_date
                        ),
            engine = CapuletEngine(
                            current_mileage = current_mileage,
                            last_service_mileage = last_service_mileage
                        ),
            tire = OctoprimeTires(TireWearArray)
        )