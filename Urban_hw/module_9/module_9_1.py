"""
Цель: научиться обращаться к функциям, как к объекту и передавать их в другие функции для вызова.

Задача "Вызов разом":
Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:
int_list - список из чисел (int, float)
*functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
Эта функция должна:
Вызвать каждую функцию к переданному списку int_list
Возвращать словарь, где ключом будет название вызванной функции, а значением - её результат работы со списком int_list.
Пункты задачи:
В функции apply_all_func создайте пустой словарь results.
Переберите все функции из *functions.
При переборе функций записывайте в словарь results результат работы этой функции под ключом её названия.
Верните словарь results.
Запустите функцию apply_all_func, передав в неё список из чисел и набор других функций.
Пример результата выполнения программы:
В примере используются следующие функции:
min - принимает список, возвращает минимальное значение из него.
max - принимает список, возвращает максимальное значение из него.
len - принимает список, возвращает кол-во элементов в нём.
sum - принимает список, возвращает сумму его элементов.
sorted - принимает список, возвращает новый отсортированный список на основе переданного.
Пример работы кода:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
Вывод на консоль:
{'max': 20, 'min': 6} {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
Примечания:
Для того, чтобы взять название функции можно обратиться к атрибуту __name__
При попытке передачи, например, списка из строк, некоторые функции могут работать некорректно или вовсе не работать. Используйте списки чисел.

"""

def apply_all_func(int_list, *functions):
    result = {}
    for function in functions:
        if function.__name__ == 'min':
            result[function.__name__] = function(int_list)
            result.update(result)
        elif function.__name__ == 'max':
            result[function.__name__] = function(int_list)
            result.update(result)
        elif function.__name__ == 'len':
            result[function.__name__] = function(int_list)
            result.update(result)
        elif function.__name__ == 'sum':
            result[function.__name__] = function(int_list)
            result.update(result)
        elif function.__name__ == 'sorted':
            result[function.__name__] = function(int_list)
            result.update(result)
    return result



print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))