class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"name:{self.restaurant_name} cuisine_type:{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is working...\n")


my_restaurant = Restaurant("OhOh", "dinner")
print(f"name:{my_restaurant.restaurant_name} cuisine:{my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant("YoYo", "Breakfast")
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

his_restaurant = Restaurant("HoHo", "Lunch")
his_restaurant.describe_restaurant()
his_restaurant.open_restaurant()
