# Распаковка параметров и параметры функции
def print_params(a=1, b='string', c=True):
    print(a, b, c)

''''''
1
''''''
print('"1"')
print_params()

print_params(1, 3)

print_params(b=25)
print_params(c=[1, 2, 3])

''''''
2
''''''
print('"2"')
values_list = [2, 'word', False]
values_dict = {'a': 3, 'b': 'test', 'c': False}
print_params(*values_list)
print_params(**values_dict)

''''''
3
''''''
print('"3"')
values_list_2 = [False, 3.14]
print_params(*values_list_2, 42)