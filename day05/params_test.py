def power(x):
    return x * x


print(power(2))


def power(x, n):
    p = 1
    while n > 0:
        p *= x
        n -= 1
    return p


print(power(2, 3))


def power(x, n=2):  # 默认参数
    p = 1
    while n > 0:
        p *= x
        n -= 1
    return p


print(power(2))  # 默认参数 n 没写，默认为2


def fn_default(x, y=1, z=2):
    return x + y - z


print(fn_default(0, 1))  # 1 为 y=1  调用，默认参数可按照顺序，不必写参数名
print(fn_default(1, z=1))  # 默认参数不按照顺序调用，需要写明参数名


# 可变参数
# 位置参数在前，默认参数在后； 把变化小的参数作为默认参数； 默认参数必须只想不变的对象
# 可变类型作为默认参数 array=【】  第二个print(fn_append())  得到 ['END' , 'END']
def fn_append(array=None):
    if array is None:
        array = []
    array.append('END')  # 追加元素到最后
    return array


print(fn_append([1, 2, 3]))
print(fn_append())  # ['END']
print(fn_append())  # ['END']

print(max(1, 2, 3, 4))

"""
void method(int... x)
"""


# * + 参数名 ；参数个数可变；可变参数被组装为tuple
def fn_sum(*numbers):
    print(numbers)
    s = 0
    for n in numbers:
        s += n
    return s


print(fn_sum(1, 2, 3, 4, 5))
# print(fn_sum())

num = [1, 2, 3, 4, 5]

print(fn_sum(num[0], num[1], num[2], num[3], num[4]))
