# 方法title()以首字母大写的方式显示每个单词，这很有用，因为经常需要将名字视为信息
name = "ada lovelace"
print(name.title())


name = "Ada Lovelace"

# 全大写
print(name.upper())

# 全小写
print(name.lower())


# 在字符串中使用变量，要在字符串中使用变量的值，可在前引号前加上字幕f再将要插入的变量放在花括号内。
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)


# 使用制表符或换行符添加空白
# 制表符
print("\tPython")

# 换行符
print("Languages:\nPython\nC\nJavaScript")

# 删除空白
print("python ".rstrip())

# 要永久删除字符串中的空白，必须将删除操作的结果关联到变量
language = "python "
print(language)
language = language.rstrip()
print(language)

# 在编程中，经常需要修改变量的值，再将新值关联到原来的变量。
# 这就是变量的值可能随程序的运行或用户输入数据而发生变化的原因所在。

# 剔除开头的空白
language = " python"
print(language)
language = language.lstrip()
print(language)


# 在用单引号括起来的字符串中，如果包含撇号，就将导致错误