"""练习"""
"""
1、
在为完成练习9-1而编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0.根据这个类创建一个名为restaurant的实例。
打印有多少人在这家餐馆就餐过，然后修改这个值病再打印它一次。
添加一个名为set_number_served()的方法，让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
添加一个名为increment_number_served()的方法，让你能够将就餐人数递增。
调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
"""


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"name:{self.restaurant_name} cuisine_type:{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is working...\n")

    def update_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment


my_restaurant = Restaurant("OhOh", "dinner")
print(f"There was {my_restaurant.number_served} person eaten dinner here.")

my_restaurant.number_served = 100
print(f"There was {my_restaurant.number_served} person eaten dinner here.")

my_restaurant.update_number_served(120)
print(f"There was {my_restaurant.number_served} person eaten dinner here.")

my_restaurant.increment_number_served(110)
print(f"There was {my_restaurant.number_served} person eaten dinner here.")
