print('''
      登  鹳  雀  楼
      -   【唐】 王之涣

      白日依山尽，
      黄河入海流。
      欲穷千里目，
      更上一层楼。
''')

import sys
print("Python version")
print(sys.version)

import time
localtime = time.asctime(time.localtime(time.time()))
print("当前时间为：" ,localtime)

a=float(input("请输入圆的半径"))
b=float(3.14*a*a)
print(b)
