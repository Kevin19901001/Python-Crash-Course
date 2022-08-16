# 使用while循环
current_count = 1
while current_count <= 5:
    print(current_count)
    current_count += 1


# 在循环中使用continue
print("\n在循环中使用continue:")
current_num = 0

while current_num < 10:
    current_num += 1

    if current_num % 2 == 0:
        continue

    print(current_num)


# 避免无限循环
x = 1

while x < 5:
    print(x)
    x += 1
