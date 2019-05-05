# print(dir('__builtins__'))    # 输出内置函数

print(abs(-4))  # 绝对值

print(max(1, 2))

print(min(-1, 0, 5, 9))

# n = int(input())
# print(int(n) + 1) # 类型转换

# n = float(input())
# print(n + 1)

print(str(123) + 'test')

a = [1, 2, 3, 1, 2, 3]
b = tuple(a)
print(b)

c = set(a)
print(c)  # 自动去掉重复值

d = set(b)
print(c, d)
print(type(a), type(b), type(c), type(d))

# 别名
absolute = abs
print(absolute(-1))


# 定义函数（规范：上下各有两行空行；小写，下划线区分单词）


def add(x, y):
    return x + y


print(add(1, 2))


def test():
    pass


# return


print(test())


def multi_return(x, y):
    """
       :param x: int...
       :param y: float...
       :return: tuple...
     """
    return x, y


m, n = multi_return(1, 2)

print(m, n)
print(multi_return(3, 4))  # 元组形式
