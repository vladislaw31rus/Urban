# Цикл for. Элементы списка. Полезные функции в цикле
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
i = 0
n = len(numbers)
for i in range(0, n):
    number = numbers[i]
    if numbers[i] == 1:
        continue
    else:
        for j in range(2, numbers[i]):
            if numbers[i] % j == 0:
                 is_prime = False
                 break
            else:
                is_prime = True
    if is_prime == True:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print("primes: ",primes)
print("not primes: ", not_primes)