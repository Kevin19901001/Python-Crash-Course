# 4.1 遍历整个列表
# 需要对列表中的每个元素都执行相同的操作时，可以使用python中的for循环。
# 通过使用for循环来打印魔术师名单中的所有名字：
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

# 4.1.2 在for循环中执行更多操作
for magician in magicians:
	print(f"{magician.title()}, that was a great trick！")
	print(f"I can wait to see your next trick, {magician.title()}.\n")

# 4.1.3 在for循环结束后执行一些操作
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can wait to see your next trick, {magician.title()}.\n")

print("Thank you everyone. That was a great magic show!")


# 4.2 避免缩进错误
# Python根据缩进来判断代码行与前一个代码行的关系


# 4.3 创建数值列表
# 4.3.1 使用函数range()
for value in range(1, 5):
	print(value)

for value in range(6):
	print(value)

# 4.3.2 使用range()创建数字列表
numbers = list(range(1, 6))
print(numbers)					# [1, 2, 3, 4, 5]

# 第3个参数：步长
even_numbers = list(range(2, 11, 2))
print(even_numbers)				# [2, 4, 6, 8, 10]

# 创建一个包含1~10的平方的列表
squares = []
for value in range(1, 11):
	square = value * value
	squares.append(square)
print(squares)					# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 4.3.3 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))				# 最小值
print(max(digits))				# 最大值
print(sum(digits))				# 求和


# 4.3.4 列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares)


# 动手试一试
# 使用一个for循环打印数1～20（含）：
digit = range(1, 21)
for value in digit:
	print(value)

for value in range(1, 21):
	print(value)


# 创建一个包含1～1000000的列表，再使用一个for循环，将这些数打印出来：
list = range(1, 1000000)
for value in list:
	print(value)