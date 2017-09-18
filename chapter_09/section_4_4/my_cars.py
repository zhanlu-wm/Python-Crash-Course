# import chapter_09.section_4_4.car
#
# my_beetle = chapter_09.section_4_4.car.Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())
#
# my_tesla = chapter_09.section_4_4.car.ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())


import chapter_09.section_4_4.car as car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())