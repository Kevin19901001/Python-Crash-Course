""" 返回值 """

""" 返回简单值 """


def get_formatted_name(first_name, last_name):
    """ 返回整洁的姓名 """
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

""" 让实参变成可选的 """


def get_formatted_name_again(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()


musician = get_formatted_name_again('jhon', 'hokker', 'lee')
print(musician)

""" 返回字典 """


def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


def build_person_again(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person_again('jimi', 'hendrix', 27)
print(musician)

musician = build_person_again('jimi', 'hendrix')
print(musician)

""" 结合使用函数和while循环 """


def get_formatted_name_with_while(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name


while True:
    print("Please tell me your name:")
    print("(Enter 'q' at any time to quit)")

    f_name = input("First name:")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name_with_while(f_name, l_name)
    print(f"Hello, {formatted_name}.\n")
