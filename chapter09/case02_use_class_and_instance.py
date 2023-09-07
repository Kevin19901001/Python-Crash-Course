"""编写一个表示汽车的类"""


class Car:
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

        """给属性指定默认值"""
        self.odometer = 0

    def get_descriptive(self):
        """返回整洁的描述性信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def get_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer} miles on it.")

    def update_odometer(self, mile_age):
        self.odometer = mile_age

    def increment_odometer(self, miles):
        """将里程表读书增加指定的量"""
        if miles < 0:
            print("里程表不允许回调！")
        else:
            self.odometer += miles


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive())
my_new_car.get_odometer()

"""直接修改属性的值"""
my_new_car.odometer = 30
my_new_car.get_odometer()

"""通过方法修改属性的值"""
my_new_car.update_odometer(60)
my_new_car.get_odometer()

"""通过方法对属性的值进行递增"""
my_new_car.increment_odometer(10_000)
my_new_car.get_odometer()
