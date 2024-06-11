# Задание "Слишком древний шифр"
x = int(input("введите число от 3 до 20: "))
array_ = []
i = 1
password = []
while i <= x:  #заполнение массива для составления пар
    array_.append(i)
    i = i + 1
for j in range(x):  #выбор первого числа пары
    a = array_[j]
    k = a
    for k in range(x):  #выбор второго числа пары
        b = array_[k]
        if (a + b) > x or a == b or a > b:  # исключение реркальных дублей, пропуск пары, если их сумма больше введенного числа
            continue
        elif x % (a + b) == 0:  # проверка кратности числа
            password.append(str(a) + str(b))
result= print("".join(password))