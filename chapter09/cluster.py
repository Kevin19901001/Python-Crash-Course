"""
将User类、Privileges类和Admin类存储在一个模块中
"""


class User:
    def __init__(self, name, age, tel, address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address
        self.login_attempts = 0

    def describe_user(self):
        print(f"name:{self.name} age:{self.age} tel:{self.tel} address:{self.address}")

    def greet_user(self):
        print(f"Hello, {self.name}!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban post']

    def show_privileges(self, user):
        print(f'The user {user.name} has {self.privileges[0]}, {self.privileges[1]}, {self.privileges[2]} privileges.')


class Admin(User):
    def __init__(self, name, age, tel, address):
        super().__init__(name, age, tel, address)
        # self.privileges = ['can add post', 'can delete post', 'can ban post']
        self.privileges = Privileges()
