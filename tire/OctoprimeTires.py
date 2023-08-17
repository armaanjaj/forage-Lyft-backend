from Tire import Tire

class OctoprimeTires(Tire):

    def __init__(self, tireWear) -> None:
        self.tireWear = tireWear

    def needs_service(self):
        return sum(self.tireWear) >= 3.0