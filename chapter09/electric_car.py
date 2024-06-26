from car import Car  # 在electric_car这个模块中导入另一个模块car

"""一组可用于表示电动汽车的类。"""


class Battery:
    """一次模拟电动汽车电瓶的简单尝试。"""

    def __init__(self, battery_size=75):
        """初始化电瓶的属性。"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息。"""
        print(f"This car has a {self.battery_size}-kWh batter.")

    def get_range(self):
        """打印一条描述电瓶续航里程的消息。"""
        if self.battery_size == 75:
            rang = 260
        elif self.battery_size == 100:
            rang = 315

        print(f"This car can go about {rang} miles on full charge.")


class ElectricCar(Car):
    """模拟电动汽车的独特之处。"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
