class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0
        self.total_cars += 1

    def accelerate(self, speed_increase):
        self.speed += speed_increase
        return f"{self.brand} {self.model} is now at {self.speed} km/h"

    def get_info(self):
        return f"Car: {self.brand} {self.model}, Speed: {self.speed} km/h"