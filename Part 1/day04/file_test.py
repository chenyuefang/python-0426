import os
import shutil

if os.path.exists('test.txt'):
    os.remove('test.txt')
else:
    print('not exits.')

# os.rename('download.py', 'download_test.py')

# shutil.copy('file_test.py', 'file_test_new.py')

# split ext:extension 扩展名
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])  # 列表生成器

print(os.path.splitext('file_test.py'))