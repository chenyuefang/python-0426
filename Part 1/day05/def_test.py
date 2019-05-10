# 导入函数
from day05.built_in_test import multi_return


print(multi_return(1, 2))


# 异常处理


def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('Error...')  # 类似于异常抛出
    if x > 0:
        return x
    else:
        return -x


# print(my_abs(-1))
print(my_abs('-1'))
