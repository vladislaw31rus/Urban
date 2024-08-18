
"""синтаксис генератора"""
def func_generator(n):
    i = 0
    while i != n:
        yield i # вместо return. эта функция возвращает значение
        i += 1
obj = func_generator(10)
print(obj) # возвращает объект генератор
for i in obj:  # возвращает значения генератора
    print(i)

#==========================================
""" обычное вычисление"""
def fibonacci_v1(n):
    result = []
    a, b, = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
        return result
fib_1 = fibonacci_v1(n=10)
print(fib_1)
for value in fib_1:
    print(value)
#==========================================
"""вычисление генератором"""
def fibonacci_v2(n):
    a, b, = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
fib_2 = fibonacci_v2(n=10)
print(fib_2)
for value in fib_2:
    print(value)
# ==========================================

"""бесконечный генератор"""
def fibonacci_v3():
    a, b, = 0, 1
    while True:
        yield a
        a, b = b, a + b
for value in fibonacci_v3():
    print(value)
    if value > 10 **6:
        break

# ==========================================
"""вывод содержимого файла"""

def read_large_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

for line in read_large_file("example.txt"):
    print(line)