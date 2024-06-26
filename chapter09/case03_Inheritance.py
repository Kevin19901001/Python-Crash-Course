"""
9.3 继承
"""
from chapter09.case02_use_class_and_instance import Car


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has {self.battery_size}-KWh battery.")

    def get_range(self):

        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f'The car can go about {range} miles on full charge.')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        """添加电动车特有的属性"""
        self.battery = Battery()

    """添加电动车特有的方法"""
    # def describe_battery(self):
    #     print(f'This car has a {self.battery_size}-KWh battery.')

    def upgrade_battery(self):
        if self.battery.battery_size != 100:
            self.battery.battery_size = 100


my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

default_car = ElectricCar('tesla', 'model y', 2019)
default_car.battery.get_range()
default_car.upgrade_battery()
default_car.battery.get_range()
