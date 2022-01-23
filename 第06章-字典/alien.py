# 6.1 一个简单的字典
alien_0 = {'color':'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 6.2 使用字典
# 6.2.2 添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 6.2.5 删除键值对
del alien_0['points']
print(alien_0)

# 6.2.7 使用get()来访问值
x_position = alien_0.get('x_position')
print(x_position)

z_position = alien_0.get('z_position')
print(z_position)   # None

z_position = alien_0.get('z_position', 'No value asigned!')
print(z_position)



# 动手试一试
# 使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。
simular_friend = {'first_name':'Iric', 'last_name':'Haris', 'city':'Wuhan'}
print(simular_friend['first_name'])
print(simular_friend['last_name'])
print(simular_friend['city'])
