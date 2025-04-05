from car import Car
import random

MIN_NUMBER = 0
MAX_NUMBER = 100

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability: float):
        super().__init__(name,fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.randint(1, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven


