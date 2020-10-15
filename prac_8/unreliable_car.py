"""Unreliable car"""

from prac_8.car import Car
from random import randint


class UnreliableCar(Car):
    """Unreliable car class"""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """drive the car based on reliability"""
        random_number = randint(1,100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven


