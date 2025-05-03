from car import Car

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
        self.battery_level = 100
        self.engine_running = False

    def accelerate(self, speed_increase):
        if not self.engine_running:
            return f"{self.brand} {self.model} engine is off. Start the engine first!"
        self.speed += speed_increase
        self.battery_level -= speed_increase * 0.2
        if self.battery_level < 0:
            self.battery_level = 0
            self.speed = 0
            self.engine_running = False
            return f"{self.brand} {self.model} ran out of battery and stopped!"
        return f"{self.brand} {self.model} is now at {self.speed} km/h, Battery: {self.battery_level}%"

    def charge(self, charge_amount):
        self.battery_level += charge_amount
        if self.battery_level > 100:
            self.battery_level = 100
        return f"{self.brand} {self.model} charged to {self.battery_level}%"

    def check_battery_status(self):
        if self.battery_level < 20:
            return f"{self.brand} {self.model} battery is low ({self.battery_level}%), please charge soon!"
        return f"{self.brand} {self.model} battery is at {self.battery_level}%"

    def estimate_range(self):
        range_km = (self.battery_level / 100) * self.battery_capacity
        return f"{self.brand} {self.model} has an estimated range of {range_km} km"

    def start_engine(self):
        if self.engine_running:
            return f"{self.brand} {self.model} engine is already running!"
        if self.battery_level <= 0:
            return f"{self.brand} {self.model} cannot start: battery is at {self.battery_level}%!"
        self.engine_running = True
        return f"{self.brand} {self.model} engine started."

    def stop_engine(self):
        if not self.engine_running:
            return f"{self.brand} {self.model} engine is already off!"
        if self.speed > 0:
            return f"{self.brand} {self.model} cannot stop: slow down to 0 km/h first!"
        self.engine_running = False
        return f"{self.brand} {self.model} engine stopped."