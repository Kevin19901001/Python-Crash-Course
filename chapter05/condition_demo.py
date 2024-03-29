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


# 5.3.2 if-else语句
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registred to vote yet?")
else:
	print("Sorry, You are too young to vote!")
	print("Please register vote as soon as you turn 18!")


# 5.3.3 if-elif-else结构：
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $25")
else:
	print("You admission cost is $40.")


# 5.3.4 使用多个elif代码块
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20
print(f"Your admission cost is ${price}.")


# 5.3.6 测试多个条件
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")



# 动手练一练：
# 创建一个外星人变量，并赋值颜色
alien_color = "green"

# 绿色，5分
if alien_color == "green":
	print("You have got 5 scores.")

alien_color = "yello"
if alien_color != "green":
	print("You have got 10 scores.")

# 3个分支：
if alien_color == "green":
	print("You have got 5 scores.")
elif alien_color == "yello":
	print("You have got 10 scores.")
else:
	print("You have got 15 scores.")

# 人生阶段：
age = 25
if age < 4:
	print("This is a baby.")
elif age < 13:
	print("This a a children.")
elif age < 20:
	print("This is a teenager.")
elif age < 65:
	print("This is an adult.")
else:
	print("This is an older.")

# 喜欢的水果：
favorate_fruits = ["banana", "orange", "apple"]
if "banana" in favorate_fruits:
	print("You really like bananas!")

if "apple" in favorate_fruits:
	print("You really like apples!")

if "orange" in favorate_fruits:
	print("You really like oranges!")


# 5.4 使用if语句处理列表：
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
	if requested_topping == "green peppers":
		print("Sorry, we are out of green peppers right now.")
	else:
		print(f"Adding {requested_topping}.")

print("\nFinished making you pizza.")


# 动手试一试：
# 以特殊方式跟管理员打招呼
users = []
if len(users) == 0:
    print("We need to find some users!")
else:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?\n")
        else:
            print("Hello, Jaden, thank you fro logging in agian.\n")

current_users = ['Kevin', 'Ketty', 'Clark', 'Kelly', 'Susan']
uppered_current_users = []
for current_user in current_users:
    uppered_current_users.append(current_user.upper())

print(uppered_current_users)

new_users = ['Mary', 'Moon', 'ketty', 'Coco', 'Clark']
for new_user in new_users:
    if new_user.upper() in uppered_current_users:
        print("This username has been used, please use another new.")
    else:
        print("This username has never been used, you can use it!")

# 练习5-11:
# 序数表示位置，如1st和2nd。序数大多以th结尾，只有1、2和3例外。
# 在一个列表中存储数字1～9
# 遍历这个列表
# 在循环中使用一个if-elif-else结构，以打印每个数字对应的序数。输出内容应为“1st 2nd 3rd 4th 5th 6th 7th 8th 9th”。
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums)

for num in nums:
    if num == 1:
        print('1st')
    elif num == 2:
        print('2nd')
    elif num == 3:
        print('3rd')
    else:
        print(f"{num}th")
