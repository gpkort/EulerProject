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


def flatten(arr, new_arr):
    print(arr)
    for i in arr:
        print('i = {}'.format(i))
        print('i is int: {}, i is list: {}'.format(type(i) is int, type(i) is list))
        if type(i) is int:
            new_arr.append(i)
            continue
        if type(i) is list:
            new_arr.append(flatten(i, new_arr))

if __name__ == "__main__":
    result = []
    flatten(factor(8), result)
    print(result)

