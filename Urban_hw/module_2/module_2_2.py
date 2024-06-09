# Условная конструкция. Операторы if, elif, else.
first = input("введи первое число: ")
second = input("введи второе число: ")
third = input("введи третье число: ")
if first == second and first == third and second == third:
    print("3")
elif first == second or first == third or second == third:
    print("2")
else:
    print("0")