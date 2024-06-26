"""在单独的文件中定义User类。"""


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
