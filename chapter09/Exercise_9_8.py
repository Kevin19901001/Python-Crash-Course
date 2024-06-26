"""
权限
"""


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban post']

    def show_privileges(self, user):
        print(f'The user {user.name} has {self.privileges[0]}, {self.privileges[1]}, {self.privileges[2]} privileges.')
