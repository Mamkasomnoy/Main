def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        sum_ = sum(args)
        a = 0
        for i in range(2, sum_ // 2 + 1):
            if sum_ % i == 0:
                a = a + 1
        if a <= 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper


@is_prime
def sum_three(*args: int):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)