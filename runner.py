import numpy as np


NUMBER = 600851475143

def eulers_1():
    return sum(num for num in range(1, 1000) if num % 3 == 0 or num % 5 == 0)


def eulers_2(*, first=2, max_fib=4000000):
    current = 2
    prev = first - 1 if current > 1 else 1
    total = 0

    def get_next(current, prev):
        return current + prev, current

    while current < max_fib:
        if current % 2 == 0:
            total = total + current
        current, prev = get_next(current, prev)

    return total


def is_prime(number: int):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i ** 2 <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i = i + 6

    return True


def factor(number):
    if is_prime(number) or number == 1:
        return [1, number]
    i = 2

    while True:
        if number % i == 0:
            first = i if is_prime(i) else factor(i)
            second = int(number / i)
            second = second if is_prime(second) else factor(second)
            return [first, second]
        i = i + 1


def get_flat_prime(primes, vals):
    for p in primes:
        if isinstance(p, int) and p is not None:
            vals.append(p)
        elif isinstance(p, list):
            vals.append(get_flat_prime(p, vals))


def get_max_primes(number):
    primes = []
    get_flat_prime(factor(NUMBER), primes)
    return  np.array([p for p in primes if p if not None]).max()


print(get_max_primes(NUMBER))
