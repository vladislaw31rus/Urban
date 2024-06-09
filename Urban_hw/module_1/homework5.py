#Неизменяемые и изменяемые объекты. Кортежи
immutable_var = 1, 2, 'sting', True     #кортеж, не изменяемый
print(immutable_var)
#immutable_var[0] = 10        #изменения не будет, т.к в нем нет переменных типа список; закоментированно, чтобы не выводило ошибку;
mutable_list = [1, 2, 'string', True]    #список, изменяемый
mutable_list[0] = 100
print(mutable_list)