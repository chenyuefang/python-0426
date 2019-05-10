"""
Java 语言：
class ClassName extends Object{
   ...//...

   int.i
}
"""


class ClassName(object):
    pass


class Human(object):

    def __init__(self, name, age, gender):  # 强制绑定
        self.name = name  # self  类似于Java 语言中的 this
        self.__age = age
        self._gender = gender


def fun_test(self):
    pass


def get_name(self):
    return self.name


def get_age(self):
    return self.__age


def set_age(self, age):
    if age > 0:
        self.__age = age
    else:
        raise ValueError('Error: age < 0')


# human = Human('Jerry', 18)  # 创建实例
# print(type(human))
#
# # 自有绑定属性
# human.name = 'Tom'  # 直接加 . 进行绑定赋值
# print(human.name)

tom = Human('Tom', 18, 'male')

print(tom.name)
# print(tom.__age)  # 私有属性
# print(tom._gender)  # 视为私有属性

print(tom.get_age())

tom.set_age(-1)

print(tom.get_age())
