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
print('x', end=' ')  # 不换行输出
print('x', end=' ')

print('x', end='')
print('x', end='')

print('k', end='\n' )  # \n : 代表换行

print(' ', end='')  # 1  ： 开头空一格
print('x', end='')  # 2
print('x')  # 3
