# from car import Car, ElectricCar
# import car
from car import Car
# from electric_car import ElectricCar
from electric_car import ElectricCar as EC  # 导入类时使用别名

# my_beetle = Car('Volkswagen', 'beetle', 2019)
# my_beetle = car.Car('Volkswagen', 'beetle', 2019)
my_beetle = Car('Volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('Tesla', 'Roadster', 2019)
# my_tesla = car.ElectricCar('Tesla', 'Roadster', 2019)
# my_tesla = ElectricCar('Tesla', 'Roadster', 2019)
my_tesla = EC('Tesla', 'Roadster', 2019)    # 使用别名EC
print(my_tesla.get_descriptive_name())
