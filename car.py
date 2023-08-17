from Servicable import Servicable
from engine.Engine import Engine
from battery.Battery import Battery
from tire.Tire import Tire

class Car(Servicable):
    
    def __init__(self, engine:Engine, battery:Battery, tire:Tire) -> None:
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()