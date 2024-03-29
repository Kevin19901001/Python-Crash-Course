"""
汽车
联系使用任意数量的关键字实参

Created: 2024-03-29
Author: FanHuanQing
"""


def build_car(brand, model, **car_info):
    car_info['brand'] = brand
    car_info['model'] = model

    return car_info


subaru = build_car('subaru', 'outback', color='blue', tow_package=True)
print(subaru)
