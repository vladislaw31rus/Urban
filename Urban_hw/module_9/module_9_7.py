def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args,**kwargs)
        if result <= 1 or result % 2 == 0:
            return "Составное"
        if result == 2:
            return "Простое"
        for i in range(3, int(result**0.5)+1, 2):
            if result % i == 0:
                return "Составное"
            return "Простое"
        return result
    return wrapper



@is_prime
def sum_three(*args):
    print(sum(args))
    return sum(args)

result = sum_three(2, 3, 7)
print(result)