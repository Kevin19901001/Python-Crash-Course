# 字典中存放列表
pizza = {'crust':'thick', 'toppings':['mushrooms', 'extra cheese']}

print(pizza)

for topping in pizza['toppings']:
    print(f"\t{topping}")
