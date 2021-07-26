# if语句
# 5.1 一个简单示例：
cars = ['audi', 'bmw', 'subru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())



# 5.2 条件测试
# 5.2.1 检查是否相等
car = 'bmw'
print(car == 'bmw')
car = 'audi'
print(car == 'bmw')


# 5.2.2 检查是否相等时忽略大小写
car = 'Toyota'
print(car == 'toyota')
print(car.lower() == 'toyota')


# 5.2.3 检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")


# 5.2.4 数值比较
age = 18
print(age == 18)

answer = 17
if answer != 42:
	print("That is not correct answer, please try again!")

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)


# 5.2.5 检查多个条件
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

#使用or来检查多个条件
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)


# 5.2.6 检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('peperoni' in requested_toppings)


# 5.2.7 检查特定值是否不包含在列表中
banned_users = ['andrew', 'caronila', 'david']
user = 'maria'
if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")


# 5.2.8 布尔表达式
game_active = True
can_edit = False



# 动手试一试
# 编写条件测试，将每个测试及对其结果的预测和实际结果打印出来。
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')


# 更多条件测试
# 检查2个字符串相等和不等
car_0 = 'subaru'
car_1 = 'Audi'
car_2 = 'audi'
car_3 = 'Audi'
print(car_0 == car_1)			# False
print(car_1 == car_2)			# False
print(car_2 == car_3)			# False
print(car_1 == car_3)			# True



# 5.3 if语句
# 5.3.1 简单的if语句
age = 19
if age >= 16:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")


# if-else语句
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registred to vote yet?")
else:
	print("Sorry, You are too young to vote!")
	print("Please register vote as soon as you turn 18!")


# if-elif-else结构：
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $25")
else:
	print("You admission cost is $40.")