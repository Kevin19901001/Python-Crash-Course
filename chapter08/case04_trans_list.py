""" 传递列表 """

def greet_users(names):
    """ 向列表中的每位用户发出简单的问候 """
    for name in names:
        print(f"Hello, {name.title()}.")

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


""" 在函数中修改列表 """
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedon']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，将其移到列表completed_models中
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"printing model:{current_design}.")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


""" 禁止函数修改列表 """
# 将列表的副本传递给函数
unprinted_designs_a = ['phone case', 'robot pendant', 'dodecahedon']
completed_models_a = []

print_models(unprinted_designs_a[:], completed_models_a)
show_completed_models(completed_models_a)
print(unprinted_designs_a)

