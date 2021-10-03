from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    started = False

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel <= 0:
                raise LowFuelError()
            else:
                self.started = True

    def move(self, distance):
        fuel_amount = self.fuel_consumption * distance
        if self.fuel-fuel_amount < 0:
            raise NotEnoughFuel()
        self.fuel -= fuel_amount

# v = Vehicle(500, 0, 15)
# v.move(1)
# v.start()
# print(v.started)


