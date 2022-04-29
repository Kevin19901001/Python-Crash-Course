# 4.5 元组
# 列表非常适合用于存储在程序运行期间可能变化的数据集。
# 列表是可以修改的，这对于处理网站的用户列表或游戏中的角色列表至关重要。
# 有时候你需要创建一系列不可修改的元素。
# 元组可以满足这种需求。
# Python将不可修改的值称为不可变的。
# 而不可变的列表保额称为元组。
demensions = (200, 50)
print(demensions[0])
print(demensions[1])

# 试图改变元组中元素的值，会报错：
# demensions[0] = 250

# 只包含一个元素的元组，需要加个逗号
my_t = (3,)
print(my_t[0])


# 遍历元组中的所有值：
for demension in demensions:
	print(demension)


# 修改元组变量
demensions = (400, 100)
for demension in demensions:
	print(demension)


# 动手试一试：
# 5中食品，存储到一个元组中
foods = ('bread', 'cake', 'egg', 'sandwich', 'cheese')

# 使用一个for循环将5种食品都打印出来
for food in foods:
	print(food)

# 尝试修改，Python会拒绝
#foods[0] = 'milk'

# 调整菜单，打印每一个元素
foods = ('bread', 'cake', 'milk', 'salad', 'cheese')
for food in foods:
	print(food)