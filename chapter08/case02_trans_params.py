""" 传递实参 """

""" 位置实参 """
def describe_pet(animal_type, pet_name):
    """ 显示宠物信息 """
    print(f"\nI have a {animal_type}.");
    print(f"My {animal_type}'s name is {pet_name.title()}.");

describe_pet('hamster', 'harry')

""" 多次调用函数 """
describe_pet('dog', 'willie')


""" 位置实参的顺序很重要 """
describe_pet('harry', 'hamster')


""" 关键字实参 """
describe_pet(animal_type='dog', pet_name='bob')


""" 默认值 """
# 使用默认值时，必须先在形参列表中列出没有默认值的形参，再列出有默认值的实参
def describe_pet_again(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.");
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet_again('gaga')


""" 等效的函数调用 """
# 一条名为“Willie的小狗
describe_pet_again("willie")
describe_pet_again(pet_name="willie")

# 一只名为Harry的仓鼠
describe_pet_again('harry', 'hamster')
describe_pet_again(animal_type='hamster', pet_name='harry')
describe_pet_again(pet_name='harry', animal_type='hamster')


""" 避免是参错误 """
# describe_pet_again()


