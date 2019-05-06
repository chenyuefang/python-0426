#   继承
#  子类继承父类的属性和方法
# 子类可以有新的属性和方法


class Human(object):
    def __init__(self, name):
        self.name = name

        def study(self):
            print('human studying...')


class Chinese(Human):

    def study(self):
        # super().study()
        print('Chinese studying...')


zhangsan = Chinese('Zhang san')

zhangsan.study()

print(zhangsan.name)
# 多态的实现   子类覆盖 override 或重写 overwrite 父类的方法
# isinstance
print(isinstance(zhangsan, Chinese))
print(isinstance(zhangsan, Human))


def fn_study(human):
    human.study()


fn_study(zhangsan)

# 鸭子类型  Duck typing


class Duck(object):

    def study(self):
        print('Duck can study?')


yellow = Duck()

fn_study(yellow)

# type 判断对象类型
print(type(abs))
print(type(fn_study))

# dir  获取对象的属性和方法
print(dir(zhangsan))

print(zhangsan.__class__)

print(dir('abc'))

print(len('abc'))
print('abc'.__len__())
