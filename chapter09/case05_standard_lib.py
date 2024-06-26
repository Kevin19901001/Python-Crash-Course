"""
9.5 Python标准库
"""
from random import randint, choice
"""randint：将两个整数作为参数，并随机返回一个位于这两个证书之间（含）的整数"""
"""在模块random中，另一个有用的函数是choice()。它将一个列表或元组作为参数，并随机返回其中一个元素。"""

print(randint(1, 10))

players = ['Charles', 'Martina', 'Michael', 'Florence', 'Eli']
first_up = choice(players)
print(first_up)
