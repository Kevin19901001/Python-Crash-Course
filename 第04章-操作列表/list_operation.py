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