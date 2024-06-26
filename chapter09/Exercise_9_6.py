"""
冰激凌小店
"""
from chapter09.Exercise_9_1 import Restaurant


class IcecreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Banana Icecream', 'Orange Icecream', 'Strawberry Icecream']

    def describe_flavors(self):
        print(f'There are {self.flavors} in IcecreamStand')


icecreamStand = IcecreamStand('MuMu', 'Snacks')
icecreamStand.describe_flavors()
