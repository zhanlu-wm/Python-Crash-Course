from chapter_09.section_3_4.car import Car
from chapter_09.section_3_4.electric_car import ElectricCar


my_car = Car('audi', 'a4', 2016)
print(my_car.get_descriptive_name())
my_car.fill_gas_tank()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
