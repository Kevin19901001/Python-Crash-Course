"""
编写一个函数，它接受顾客要在三明治中添加的一系列食材。
这个函数只有1个形参（它收集函数调用中的所有食材），并打印一条消息，对顾客点的三明治进行概述。
调用这个函数3次，每次都提供不同数量的实参。
"""


def desc_sandwich(*toppings):
    print("Making a pizza with following toppings:")
    for topping in toppings:
        print(f"--{topping}")


desc_sandwich("mushrooms")
print("----------------------分割线----------------------")
desc_sandwich("mushrooms", "green peppers")
print("----------------------分割线----------------------")
desc_sandwich("mushrooms", "green peppers", "extra cheese")
