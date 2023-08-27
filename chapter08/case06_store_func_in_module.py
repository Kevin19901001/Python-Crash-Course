
"""将函数存储在模块中"""
# 导入模块
# import case05_trans_any_params
# print('导入模块')
# case05_trans_any_params.make_pizza_again(16, 'pepperino')


# 导入特定的函数
# from case05_trans_any_params import make_pizza_again
# print('导入特定的函数')
# make_pizza_again(12, 'mushrooms', 'green peppers', 'extra chesse')


# 使用as给函数指定别名
# from case05_trans_any_params import make_pizza_again as make_pizza
# print('使用as给函数指定别名')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 导入模块中的所有函数
from case05_trans_any_params import *
print('导入模块中的所有函数')
make_pizza('pepperino')
make_pizza_again('mushrooms', 'green peppers', 'extra cheese')
make_pizza_again_and_again(16, 'mushrooms', 'green peppers', 'extra cheese')
