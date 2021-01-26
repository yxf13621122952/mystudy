# -*- coding: utf-8 -*-
"""
-----------------------------------
# @Time    : 2021/1/26 13:52
# @Author  : 闫雪峰
# @Email   : 13621122952@163.com
# @File    : animal.py
# @Software: PyCharm
-----------------------------------
"""

"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
"""


class Animal:  #类名 驼峰命名法

    # 构造方法，在类实例化的时候自动执行
    def __init__(self, name, color, age, sex):
        # 定义实例变量
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    # 动态方法
    def talk(self):
        print("{}会叫".format(self.name))

    def run(self):
        print("{}会跑".format(self.name))


if __name__ == '__main__':
    # 实例化
    animal = Animal("coco", "black", 3, "公")
    animal.talk()
    animal.run()
