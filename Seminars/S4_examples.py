# import os

# path = os.path.join('folder', 'file.txt')
# with open(path, 'r') as f:
#     pass

# from pathlib import Path

# path = Path.home
# with open(path, 'r') as f:
#     pass

# Режимы работы с файлами

# a (add, append) - добавить и читать
# w (write) - писать (перезаписать)
# r (read) - читать

# path = 'folder/file.txt'
# with open(path, 'r') as data:
#    for line in data:
#     print(line)


path = r'folder/file.txt'
with open(path, 'w') as data:
   data.write('asd')
   