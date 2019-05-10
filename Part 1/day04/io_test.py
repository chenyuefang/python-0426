f=open('C:/new 1.txt',encoding='utf-8')  # encoding='utf-8' 读取其他类型的文本
print(f.read())
f.close()

with open('C:/new 1.txt',encoding='utf-8') as f:
    # print(f.read(3))
    pass

with open('C:/new 1.txt',encoding='utf-8') as f:
    pass
    # line = f.readline()
    # while line:
    #     print(line.strip())
    #     line = f.readline()

s = ' Hello, World! '
# print(s.strip())
# print(s.lstrip())  # l:left
# print(s.rstrip())  # r:right

with open('C:/new 1.txt', encoding='utf-8') as f:
    for x in f:
        print(x.strip())

with open('C:/new 1.txt', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())