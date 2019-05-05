import string

arr=input()


def fn_str(arr):
    while (arr in string.ascii_letters):
        if arr in string.ascii_uppercase:
            n: int = 0
            print('ascii_uppercase')
            n += n
            print(n)
        elif arr in string.ascii_lowercase:
            m: int = 0
            print('ascii_lowercase')
            m += m
            print(m)
    return -1
