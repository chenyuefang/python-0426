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

print(isinstance(zhangsan, Chinese))
print(isinstance(zhangsan, Human))


def fn_study(human):
    human.study()


fn_study(zhangsan)


class Duck(object):

    def study(self):
        print('Duck can study?')


yellow = Duck()

fn_study(yellow)

print(type(abs))
print(type(fn_study))

print(dir(zhangsan))

print(zhangsan.__class__)

print(dir('abc'))

print(len('abc'))
print('abc'.__len__())
