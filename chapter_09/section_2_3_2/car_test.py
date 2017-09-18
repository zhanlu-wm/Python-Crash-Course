from chapter_09.section_2_3_2.car import Car

my_new_car = Car('audi', 'a4', '2016')
print(my_new_car.get_descriptive_name())

# 通过方法修改属性的值
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.update_odometer(20)
my_new_car.read_odometer()