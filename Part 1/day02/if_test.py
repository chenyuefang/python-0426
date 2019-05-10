score = 70

if score > 60:
    print('pass')

if score > 60:
    print('pass')
else:
    print('failed')

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
else:
    print('C')


print('x')
print('x')

# python 不换行输出 x ？

print('x', end='\n')
print('a', end=' ')  # 不换行输出
print('b', end=' ')

print('c', end='')
print('d', end='')

print('e', end='\n' )  # \n : 代表换行

print(' ', end='')  # 1  ： 开头空一格
print('f', end='')  # 2
print('g')  # 3

