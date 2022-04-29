# 列表给列表指定一个表示复数的名称是一个不错的选择
bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)

# 列表是有序的,通过索引访问。通过复数索引逆序访问。
print(bicycles[0])
print(bicycles[-1])

names = ['Curry', 'Durant', 'Harden', 'Ervin']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

message = "\n\tHow's it going!"
print(f"{names[0]}\n\tHow's it going!")
print(f"{names[1]}\n\tHow's it going!")
print(f"{names[2]}\n\tHow's it going!")
print(f"{names[3]}\n\tHow's it going!")


# 3.2 修改、添加和删除元素
motorcycles = ['honda', 'yamaha', 'suzuka']
print(motorcycles)

# 3.2.1 修改列表元素
motorcycles[0] = 'ducati'
print(motorcycles)

# 3.2.2 在列表中添加元素
# 1 在末尾添加
motorcycles = ['honda', 'yamaha', 'suzuka']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

# 2 在列表中插入元素
motorcycles = ['honda', 'yamaha', 'suzuka']
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 3.2.3 从列表中删除元素
# 1 使用del语句：删除后无法访问到这个值
motorcycles = ['honda', 'yamaha', 'suzuka']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# 2 使用pop()删除：删除列表末尾的元素，并接着使用它的值
motorcycles = ['honda', 'yamaha', 'suzuka']
print(motorcycles)
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)

# 3 弹出任意位置的元素
motorcycles = ['honda', 'yamaha', 'suzuka']
print(motorcycles)
first_owned_motorcycle = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned_motorcycle}.")
print(motorcycles)

# 4 根据值删除元素：在只知道需要删除的元素的值的时候适用
motorcycles = ['honda', 'yamaha', 'suzuka']
print(motorcycles)
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(f"A {too_expensive.title()} is too expensive for me.")
print(motorcycles)

# 联系3-4：嘉宾名单
guests = ['Bob', 'Amy', 'Jack', 'Kevin']
print(f"Hi! {guests[0]}, let's have a dinner!")
print(f"Hi! {guests[1]}, let's have a dinner!")
print(f"Hi! {guests[2]}, let's have a dinner!")
print(f"Hi! {guests[3]}, let's have a dinner!")
print(f"{guests[0]} will not come.")
guests[0] = 'Jhon'
print(f"Hi! {guests[0]}, let's have a dinner!")
print(f"Hi! {guests[1]}, let's have a dinner!")
print(f"Hi! {guests[2]}, let's have a dinner!")
print(f"Hi! {guests[3]}, let's have a dinner!")
print("I have found a lager desk!")
guests.insert(0, 'Micheal')
guests.insert(2, 'Hellen')
guests.append('Green')
print(f"Hi! {guests[0]}, let's have a dinner!")
print(f"Hi! {guests[1]}, let's have a dinner!")
print(f"Hi! {guests[2]}, let's have a dinner!")
print(f"Hi! {guests[3]}, let's have a dinner!")
print(f"Hi! {guests[4]}, let's have a dinner!")
print(f"Hi! {guests[5]}, let's have a dinner!")
print(f"Hi! {guests[6]}, let's have a dinner!")

print("Now, I could only invite 2 guests.")
poped_guest = guests.pop()
print(f"Oh, {poped_guest}, I am sorry, I can not invite you.")
poped_guest = guests.pop()
print(f"Oh, {poped_guest}, I am sorry, I can not invite you.")
poped_guest = guests.pop()
print(f"Oh, {poped_guest}, I am sorry, I can not invite you.")
poped_guest = guests.pop()
print(f"Oh, {poped_guest}, I am sorry, I can not invite you.")
poped_guest = guests.pop()
print(f"Oh, {poped_guest}, I am sorry, I can not invite you.")

print(guests)

print(f"{guests[0]}, you are still invited.")
print(f"{guests[1]}, you are still invited.")



del guests[0]
del guests[0]

print(guests)


# 3.3 组织列表
# 3.3.1 使用sort()对列表永久排序
cars = ['bmw', 'audi', 'toyota', 'sabaru']
cars.sort()
print(cars)
# 按照字母顺序相反的方向排序
cars = ['bmw', 'audi', 'toyota', 'sabaru']
cars.sort(reverse=True)
print(cars)

# 使用sorted()对列表临时排序
cars = ['bmw', 'audi', 'toyota', 'sabaru']
print("\nhere is the origin list:")
print(cars)

print("\nhere is the sorted list:")
print(sorted(cars))	# 不改变原列表顺序

print("\nhere is the origin list again:")
print(cars)

# 3.3.3 倒着打印列表
cars = ['bmw', 'audi', 'toyota', 'sabaru']
cars.reverse()	# 永久性地改变了列表元素顺序
print(cars)

# 3.3.4 确定列表的长度
cars = ['bmw', 'audi', 'toyota', 'sabaru']
print(len(cars))


# 动手试一试：练习 3-8
places = ['贝加尔湖', '武夷山', '西湖', '黄果树瀑布', '龙门石窟']
print(places)						# ['贝加尔湖', '武夷山', '西湖', '黄果树瀑布', '龙门石窟']

sorted_places = sorted(places)		# 按字母顺序临时排序
print(sorted_places)				# ['武夷山', '西湖', '贝加尔湖', '黄果树瀑布', '龙门石窟']

sorted_places.reverse()				# 将临时排序的列表倒序
print(sorted_places)				# ['龙门石窟', '黄果树瀑布', '贝加尔湖', '西湖', '武夷山']

sorted_places.reverse()				# 再次倒序
print(sorted_places)				# ['武夷山', '西湖', '贝加尔湖', '黄果树瀑布', '龙门石窟']

places.sort()						# 将原列表按字母顺序永久性排序
print(places)						# ['武夷山', '西湖', '贝加尔湖', '黄果树瀑布', '龙门石窟']

places.sort(reverse=True)			# 将已永久性排序的列表永久性倒序
print(places)						# ['龙门石窟', '黄果树瀑布', '贝加尔湖', '西湖', '武夷山']

places_num = len(places)
print(places_num)					# 5

cities = ['Beijing', 'shanghai', 'Wuhan', 'Hangzhou', 'Chengdu']
first_city = cities[0]				# 通过下标访问
print(first_city)					# Beijing

cities[0] = 'Shenzhen'				# 修改列表元素
print(cities)						# ['Shenzhen', 'shanghai', 'Wuhan', 'Hangzhou', 'Chengdu']

cities.append('Guangzhou')			# 向列表末尾追加元素
print(cities)						# ['Shenzhen', 'shanghai', 'Wuhan', 'Hangzhou', 'Chengdu', 'Guangzhou']

cities.insert(2, 'Tianjin')			# 向列表中插入元素
print(cities)						# ['Shenzhen', 'shanghai', 'Tianjin', 'Wuhan', 'Hangzhou', 'Chengdu', 'Guangzhou']

del cities[5]						# 使用del删除列表元素
print(cities)						# ['Shenzhen', 'shanghai', 'Tianjin', 'Wuhan', 'Hangzhou', 'Guangzhou']

poped_city = cities.pop(2)			# 使用pop删除列表元素
print(poped_city)					# Tianjin
print(cities)						# ['Shenzhen', 'shanghai', 'Wuhan', 'Hangzhou', 'Guangzhou']

cities.remove('shanghai')			# 使用remove删除列表元素
print(cities)						# ['Shenzhen', 'Wuhan', 'Hangzhou', 'Guangzhou']

cities.sort()						# 使用sort()对列表永久排序
print(cities)						# ['Guangzhou', 'Hangzhou', 'Shenzhen', 'Wuhan']

print(sorted(cities))				# 使用sorted()对列表临时排序

cities.reverse()
print(cities)						# 倒序打印

print(len(cities))					# 列表长度


# 3.4使用列表时避免索引错误
print(cities[-1])					# Guangzhou