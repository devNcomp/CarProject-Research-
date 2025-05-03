from car import Car
from electric_car import ElectricCar

# Creating instances
car1 = Car("Toyota", "Camry")
ev1 = ElectricCar("Tesla", "Model S", 400)

# Simple output
print(car1.accelerate(50))
print(ev1.start_engine())
print(ev1.accelerate(30))