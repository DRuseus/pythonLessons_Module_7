import os
import time

print(os.getcwd())
# >>> D:\PyProjects\pythonLessons_Module_7\Module_7_5 (Это мой вывод)

# Создаются директории и файлы в рабочей директории "Module_7_5" домашнего задания
if not os.path.isdir('directory_0'):
    os.mkdir('directory_0')
    file = open(r'directory_0\first_text.txt', 'w')
    file.write('size of this file is 29 bytes')
    file.close()
if not os.path.isdir(r'directory_0\directory_1\directory_2'):
    os.makedirs(r'directory_0\directory_1\directory_2')
    file = open(r'directory_0\directory_1\second_text.txt', 'w')
    file.write('Hello')
    file.close()

for dirpath, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        print(f'Обнаружен файл: {filename}', '\n' +
              f'Путь:', file := os.path.join(dirpath, filename), '\n' +
              f'Файл "{filename}" последний раз был изменён:', time.ctime(os.path.getmtime(file)), '\n' +
              f'Размер файла "{filename}":', os.path.getsize(file), 'bytes', '\n' +
              f'Родительская категория:',
              dirpath)  # Путь так-то уже известен и находится в переменной "dirpath"
        print()  # Просто для разделения найденых файлов
