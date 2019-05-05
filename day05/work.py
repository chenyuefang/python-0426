# 1
import string

a = str(input())


def fn_str(a):
    while a in string.ascii_letters:
        if a in string.ascii_uppercase:
            n: int = 0
            print('ascii_uppercase')
            n += n
            print(n)
        elif a in string.ascii_lowercase:
            m: int = 0
            print('ascii_lowercase')
            m += m
            print(m)
    return -1


# 2

li = [1, 2, 3, 4, 5, 1, 2, 3]

li = list(set(li))

print(li)


# 3.


def fn_fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fn_fibonacci(n - 1) + fn_fibonacci(n - 2)


print(fn_fibonacci(10))
