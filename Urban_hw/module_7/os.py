import os
"""
https://docs.python.org/3/library/os.html
документация модуля os
"""
print('текущая директория: ',os.getcwd()) # текущая директория
if os.path.exists('second'):  # если директория существует
    os.chdir('second')  # переходим в директорию second
else:
    os.mkdir('second')  # создаем директорию second
    os.chdir('second')  # переходим в директорию second
print('текущая директория: ',os.getcwd()) # текущая директория
# os.makedirs(r'third\fourth') # содали директорию third, а в ней fourth, r-строка обязательно
# print(os.listdir()) # вывести список директорий
# for i in os.walk('.'):  # посмотреть вложенность директорий, точка-текущия директория
#     print(i)
os.chdir(r'C:\Users\vladi\PycharmProjects\Urban_hw\module_7')  # переходим в директорию module_7
print('текущая директория: ',os.getcwd()) # текущая директория
# сотрировка на файлы и папки
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
# print(os.listdir())
print(dirs)
print(file)
#
# os.startfile(file[6]) # отктыли файл openfile.txt
# print(os.stat(file[6]))  # инфо о файле
# os.system('pip install random2')  # передали в коммандную строку комманду

