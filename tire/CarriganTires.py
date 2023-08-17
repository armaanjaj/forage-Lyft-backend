from Tire import Tire

class CarriganTires(Tire):

    def __init__(self, tireWear) -> None:
        self.tireWear = tireWear

    def needs_service(self) -> bool:
        for tire in self.tireWear:
            if tire >= 0.9:
                return True
        return False