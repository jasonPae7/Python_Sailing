# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
# # my_new_car = Car('Audi','A4',2026)
# # print(my_new_car.get_descriptive_name())
#
# class Battery:
#     def __init__(self, battery_size = 40):
#         self.battery_size = battery_size
#     def get_range(self):
#         if self.battery_size == 40:
#             range = 150
#         elif self.battery_size == 65:
#             range = 225
#         print(f"This car can go about {range} km/h on a full charge")
#     def upgrade_battery(self):
#         if self.battery_size < 65:
#             self.battery_size = 65
#
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make,model,year)
#         self.battery = Battery();
#     def describe_battery(self):
#         self.battery.get_range()
# ecar = ElectricCar('ecar','model',2016)
# ecar.describe_battery()
# ecar.battery.upgrade_battery()
# ecar.describe_battery()
from random import random

# from Car import ElectricCar
# my_leaf = ElectricCar('Nissan','leaf',2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()

# from Car import Car,ElectricCar
# my_mustang = Car('ford','mustang',2024)
# print(my_mustang.get_descriptive_name())

# from random import randint
# print(randint(1,6))
#
# from random import choice
# playeers = ['charles','martina','michael','florence','eli']
# first_up = choice(playeers)
# print(first_up)

import random

outcomes = {
    'head':0,
    'tail':0,
}

sides = list(outcomes.keys())

for i in range(10000):
    outcomes[random.choice(sides)] += 1
print('Heads:',outcomes['head'])
print('Tails:',outcomes['tail'])