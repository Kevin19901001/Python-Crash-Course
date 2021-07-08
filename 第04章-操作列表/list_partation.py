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