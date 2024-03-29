"""
用户简介
联系使用任意数量的关键字实参

Created: 2024-03-29
Author: FanHuanQing
"""


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info


user_profile = build_profile('HuanQing', 'Fan', city='Wuhan', company='Cpic', job='Tester')
user_brief = build_profile('AnQiang', 'Shou', age=27, major='Python', job='Tester')

print(user_profile)
print(user_brief)
