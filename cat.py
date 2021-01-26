# -*- coding: utf-8 -*-
"""
-----------------------------------
# @Time    : 2021/1/26 14:46
# @Author  : 闫雪峰
# @Email   : 13621122952@163.com
# @File    : cat.py
# @Software: PyCharm
-----------------------------------
"""
from animal import Animal

"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
"""


class Cat(Animal):  # 继承动物类
    def __init__(self, hair):
        # 添加一个新属性，毛发
        self.hair = hair
        # 继承父类的属性
        super().__init__("jojo", "black", 2, "公")

    # 添加一个新的方法
    def CatchMouse(self):
        print("{}捉老鼠".format(cat.name))

    # 重写父类方法
    def talk(self):
        print("{}喵喵叫".format(cat.name))


if __name__ == '__main__':
    cat = Cat("短毛")
    cat.CatchMouse()
    cat.talk()
    print("姓名：{}\n颜色：{}\n年龄：{}\n性别：{}\n毛发：{}".format(cat.name, cat.color, cat.age, cat.sex, cat.hair))
