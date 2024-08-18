sum_ = 0


def inside(sel_):
    global sum_
    if isinstance(sel_, str):
        sum_ += int(len(sel_))
    elif isinstance(sel_, int):
        sum_ += int(sel_)
    elif isinstance(sel_, tuple):
        sel_temp = []
        for k in range(0, len(sel_)):
            sel_temp.append(sel_[k])
        cell_type(sel_temp)
    elif isinstance(sel_, dict):
        cell_type(sel_)
    elif isinstance(sel_, set):  # {(2, 'Urban', ('Urban2', 35))}
        for item in sel_:
            inside(item)
    elif isinstance(sel_, list):
        cell_type(sel_)


def cell_type(sel):
    global sum_
    if isinstance(sel, int):
        inside(sel)
    elif isinstance(sel, str):
        for j in range(0, len(sel)):
            sel_ = sel[j]
            sum_ += int(len(sel_))
    elif isinstance(sel, tuple):  # (6, {'cube': 7, 'drum': 8})
        for j in range(0, len(sel)):
            sel_ = sel[j]
            inside(sel_)
    elif isinstance(sel, list):  # [1, 2, 3]
        for j in range(0, len(sel)):
            sel_ = sel[j]
            inside(sel_)
    elif isinstance(sel, dict):  # {'a': 4, 'b': 5}
        sel = list(sel.items())
        cell_type(sel)


def calculate_structure_sum(*args):
    for i in range(len(args)):
        sel = args[i]
        cell_type(sel)
    return sum_


data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

result = calculate_structure_sum(data_structure)
print(result)

"@"""""
Дополнительное практическое задание по модулю: "Подробнее о функциях."

Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности


Задание "Раз, два, три, четыре, пять .... Это не всё?":
Наши студенты, без исключения, - очень умные ребята. Настолько умные, что иногда по утру сами путаются в том, что намудрили вчера вечером.
Один из таких учеников уснул на клавиатуре в процессе упорной учёбы (ещё и трудолюбивые). Тем не менее, даже после сна, его код остался рабочим и выглядел следующим образом:

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

Увидев это студент задался вопросом: "А есть ли универсальное решение для подсчёта суммы всех чисел и длин всех строк?"
Да, выглядит страшно, да и обращаться нужно к каждой внутренней структуре (списку, словарю и т.д.) по-разному.

Ученику пришлось каждый раз использовать индексацию и обращение по ключам - универсального решения для таких структур он не нашёл.

Помогите сокурснику осуществить его задумку.

Что должно быть подсчитано:
Все числа (не важно, являются они ключами или значениям или ещё чем-то).
Все строки (не важно, являются они ключами или значениям или ещё чем-то)

Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

Входные данные (применение функции):
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


Выходные данные (консоль):
99


Примечания (рекомендации):
Весь подсчёт должен выполняться одним вызовом функции.
Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
Для определения типа данного используйте функцию isinstance.
"@"""
