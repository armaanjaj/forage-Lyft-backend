from Servicable import Servicable
from engine.Engine import Engine
from battery.Battery import Battery

class Car(Servicable):
    
    def __init__(self, engine:Engine, battery:Battery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return super().needs_service()