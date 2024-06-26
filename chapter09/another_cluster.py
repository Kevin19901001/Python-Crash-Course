"""将Privileges类和Admin类存储在另一个模块中。"""
from user import User


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
