# 9.1.1 创建Dog类
class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """迷你小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")


my_dog = Dog("Willie", 6)
"""1、访问属性"""
print(f"My dog's is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

"""2、调用方法"""
my_dog.sit()
my_dog.roll_over()

"""3、创建多个实例"""
your_dog = Dog("Lucy", 3)
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()

"""联系"""
"""1、创建Restaurant类，设置属性和方法"""

"""2、创建3个Restaurant类的实例，并调用方法"""

"""3、创建1个User类，设置彗星和方法"""
