"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle
from engine import Engine


class Car(Vehicle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.engine = None

    def set_engine(self, eng):
        self.engine = eng


# c = Car(200, 500, 15)
# c.set_engine(Engine(5.3, 4))
# print(c.engine)

