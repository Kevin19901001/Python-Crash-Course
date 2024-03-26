"""传递任意数量的实参"""


def make_pizza(*toppings):
    """打印顾客的所有配料"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza_again(*toppings):
    print('Making a pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')


make_pizza_again('pepperoni')
make_pizza_again('mushrooms', 'green peppers', 'extra cheese')

"""结合使用位置实参和任意数量实参"""


def make_pizza_again_and_again(size, *toppings):
    print(f'\nMaking a {size}-inch pizza with following toppings:')
    for topping in toppings:
        print(f'- {topping}')


make_pizza_again_and_again(16, 'pepperoni')
make_pizza_again_and_again(12, 'mushrooms', 'green peppers', 'extra cheese')

"""使用任意数量的关键字实参"""


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
