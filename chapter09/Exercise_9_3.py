class User:
    def __init__(self, name, age, tel, address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

    def describe_user(self):
        print(f"name:{self.name} age:{self.age} tel:{self.tel} address:{self.address}")

    def greet_user(self):
        print(f"Hello, {self.name}!")


amy = User("Amy", 25, "13111111111", "New York")
bob = User("Bob", 24, "13211111111", "Chicago")
chris = User("Chris", 23, "13311111111", "Huston")
amy.describe_user()
amy.greet_user()

bob.describe_user()
bob.greet_user()

chris.describe_user()
chris.greet_user()
