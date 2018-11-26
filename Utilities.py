import numpy as np
import math

BASIC_PRIMES = np.array([1, 2, 3, 5, 7, 11, 13, 17, 19])


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


def get_triangle(number: int):
    # (n+1)
    # (2)
    last = number + 1
    while True:
        number += last
        last += 1
        yield number


def get_definite_triangle(number):
    number += 1
    return int(math.factorial(number) / (2 * math.factorial(number - 2)))


def is_prime(number: int):
    if number <= 1:
        return False
    if number <= BASIC_PRIMES.max():
        return number in BASIC_PRIMES

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i ** 2 <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i = i + 6

    return True


def get_factors(number: int):
    ret = list()
    flatten(factor(number), ret)
    return ret


def all_factors(number: int):
    factors = list()

    if is_prime(number) or number == 1:
        factors = [1, number]
    else:
        i = 1

        while i < number:
            if number % i == 0:
                factors += [i, int(number/i)]
            i += 1

    return list(set(factors))


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


def flatten(arr, new_arr):
    for i in arr:
        if type(i) is int:
            new_arr.append(i)
        if type(i) is list:
            new_arr.append(flatten(i, new_arr))

    while None in new_arr:
        new_arr.remove(None)


def get_linear_max_product(grid):
    max_val = 0
    length = len(grid)

    for i in range(0, length):
        j = 0
        while j + 3 < length:
            tot = np.array(grid[i][j:j + 4]).prod()
            max_val = tot if tot > max_val else max_val
            j = j + 1

    return max_val


def get_all_prime_factors(number):
    if is_prime(number):
        return [number]

    primes = list()

    primegen = get_primes(1)
    p = next(primegen)

    while p < number:
        if number % p == 0:
            primes.append(p)
        p = next(primegen)

    return primes


def get_number_of_factors(number):
    if is_prime(number):
        return 2

    exponents = np.array([])
    primes = get_all_prime_factors(number)
    print(primes)

    for p in primes:
        exp = 1
        p_new = math.pow(p, exp)

        while p_new < number:
            if number % p_new == 0:
                print(exp)
                np.append(exponents, exp)
            exp += 1
            p_new = math.pow(p, exp)

        exponents += 1
        print(exponents)
        return int(exponents.prod())


def get_diagonal_max_product(grid, reverse=False):
    length = len(grid)
    max_val = 0
    j_start = 0
    j_end = 3 if reverse else length - 3
    increment = 1

    if reverse:
        j_start = length - 1
        j_end = 3
        increment = -1

    for i in range(0, length - 3):
        for j in range(j_start, j_end, increment):
            tot = grid[i][j] * \
                  grid[i + 1][j + increment] * \
                  grid[i + 2][j + (2*increment)] * \
                  grid[i + 3][j + (3*increment)]
            max_val = tot if tot > max_val else max_val

    return max_val


if __name__ == "__main__":
    result = list()
    flatten([1, [2, [3, 4, [5]]]], result)




    print(result)

