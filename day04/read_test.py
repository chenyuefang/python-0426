import os

from urllib.request import urlopen

# f = open('C:/new 1.txt', encoding='utf-8')
# print(f.read())
# f.close()

with open('C:/new 1.txt', encoding='utf-8') as f:
    # print(f.read(3))
    pass

with open('C:/new 1.txt', encoding='utf-8') as f:
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
        # print(x.strip())
        pass

with open('C:/new 1.txt', encoding='utf-8') as f:
    for line in f.readlines():
        # print(line.strip())
        pass

with open('1.jpg', 'rb') as f:
    # print(f.read())
    pass

# print(os.getcwd())  # current working directory

with urlopen('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4') as f:
    for line in f.readlines():
        line = line.decode('utf-8')
        if 'img class=""' in line:
            print(line.strip()[len('<img class="" src="'):len(line.strip())-1])