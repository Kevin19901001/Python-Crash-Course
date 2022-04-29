# 8.1 定义函数

def greet_user():
    """ 显示简单的问候语 """
    print("Hello");

greet_user()


''' 向函数传递信息 '''
def greet_user_again(username):
    """ 显示简单的问候语 """
    print(f"Hello, {username.title()}!");

greet_user_again("Lily")


''' 形参和实参 '''

