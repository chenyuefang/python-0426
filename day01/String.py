
s = 'Hello, World!'
s = 'hello, World!'

print(s[0])  #  第一个元素

print(s * 3)   #  将字符串重复三次

print(s[4:8])  # 从第四个元素起，到第八个元素前结束

print('He' in s)

print(s.capitalize())

print(s.center(20, '-'))  #   在字符串两边用-填充，一共20位

print(s.zfill(20))  # zero fill  在元素的开头用0填充至20位

print(s.count('l'))  # 计算‘l’在字符串中出现的次数

print(s.endswith('!', 0, 1))   # 在第0个和第一个的元素是否以！结尾

print(s.find(',', 10, 13))   


