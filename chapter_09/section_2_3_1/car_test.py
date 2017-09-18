from chapter_09.section_2_3_1.car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# 直接修改对象属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()