"""
管理员
"""
from chapter09.Exercise_9_3 import User
from chapter09.Exercise_9_8 import Privileges


class Admin(User):
    def __init__(self, name, age, tel, address):
        super().__init__(name, age, tel, address)
        # self.privileges = ['can add post', 'can delete post', 'can ban post']
        self.privileges = Privileges()

        # def show_privileges(self):
    # print(f'The user {self.name} has {self.privileges[0]}, {self.privileges[1]}, {self.privileges[2]} privileges.')


admin = Admin('Kevin', 22, '13257117557', 'Hubei Wuhan')
# admin.show_privileges()
admin.privileges.show_privileges(admin)
