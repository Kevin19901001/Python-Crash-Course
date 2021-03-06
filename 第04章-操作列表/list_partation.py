# 4.4 使用列表的一部分
players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])			# 从第1个开始到第4个
print(players[2:])			# 从第3个开始到最后一个


# 遍历切片
print('Here are the first three players on my team:')
for player in players[:3]:
	print(player.title())


# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
print('My favorite foods are:')
print(my_foods)

friend_foods = my_foods[:]			# 全复制
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print('My favorite foods are:')
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


# 练习：
# 切片 - 选择你在本章编写的一个程序，在末尾
# 添加几行代码，以完成如下任务：
# 打印消息“The first thress items in the list are:”，
# 再使用切片来打印列表的前3个元素
print("The first three items in the list are:")
for value in players[:3]:
	print(value)


# 打印消息“Three items from the middle of the list are:”，
# 再使用切片来打印列表的中间3个元素
print("\nThree items from the middle of the list are:")
for value in players[1:4]:
	print(value)


# 你的批萨，我的批萨：
# 创建批萨列表的副本
# 并将其赋值给变量friends_pizaas,
# 再完成如下任务
# 在原来的pissa列表中增加一种批萨
# 在列表friends_pizzas中增加另一种pizza
# 核实有2个不同的列表
# 为此，打印消息“My favorite pizzas are:”
# 再使用一个for循环打印第一个列表
# 打印消息“My friend's favorite pizzas are:”
# 再使用一个for循环来打印第2个列表
my_pizzas = ['pizza', 'falafel', 'carrot cake']
print("My favorite pizzas are:")
friend_pizzas = my_pizzas[:]

my_pizzas.append('cannoli')
for pizza in my_pizzas:
	print(pizza)

friend_pizzas.append('ice_cream')
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
