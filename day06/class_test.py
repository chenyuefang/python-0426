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

    def __init__(self, name, age):  # 强制绑定
        self.name = name   # self  类似于Java 语言中的 this
        self.age = age


human = Human('Jerry', 18)  # 创建实例
print(type(human))

# 自有绑定属性
human.name = 'Tom'  # 直接加 . 进行绑定赋值
print(human.name)
