from pprint import pprint

name = 'openfile.txt'
file = open(name, 'r') # r,w,a == read,write,append
print(file)
pprint(file.read())
file.close()

name = 'openfile2.txt'
file = open(name, 'w') # r,w,a == read,write,append
file.write('test  write')
file.close()

name = 'openfile2.txt'
file = open(name, 'a') # r,w,a == read,write,append
file.write('\ntest  append')
file.close()

name = 'openfile2.txt'
file = open(name, 'a') # r,w,a == read,write,append
file.write('\ntest  append2')
file.close()

name = 'openfile2.txt'
file = open(name, 'r') # r,w,a == read,write,append
print(file.tell()) # Возвращает текущую позицию курсора
pprint(file.read())
print(file.seek(8))# задает позицию курсора
pprint(file.read())
file.close()