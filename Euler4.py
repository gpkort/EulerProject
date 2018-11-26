import numpy as np
import math
import Utilities as ut

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 
9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.
'''


def euler_4():
    def factor(number):
        for i in range(100, 1000):
            if number % i == 0:
                if 99 < (number / i) < 1000:
                    return True
        return False

    palindromes = [p for p in range(100000, 1000000) if str(p) == (str(p))[::-1]]

    return np.array([p for p in palindromes if factor(p)]).max()


'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def validate_number(number, max=20):
    for x in range(1, max + 1):
        print('For {} the remainder {}'.format(x, number % x))


def euler_5(target: int):
    factors = [i for i in range(2, target + 1)]
    for i in range(0, target - 1):
        num = factors[i]
        for j in range(i + 1, target - 1):
            if factors[j] % num == 0:
                factors[j] = int(factors[j] / num)

    return np.prod(factors)


"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum 
is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def euler_6(target: int):
    target = target + 1
    squares = np.array([i ** 2 for i in range(1, target)])
    sums = np.array([i for i in range(1, target)])
    return np.abs(squares.sum() - sums.sum() ** 2)


"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""


def euler_7(limit: int):
    i = 2
    found = 0
    prime = 0

    while found < 10001:
        if ut.is_prime(i):
            found = found + 1
            prime = i
        i = i + 1
    return prime


def array_prod(arr):
    tot = 1

    try:
        for i in arr:
            tot = int(i) * int(tot)
    except RuntimeWarning:
        print('Warning was raised as an exception!')

    return tot


"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""

digits = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843' + \
         '8586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557' + \
         '6689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749' + \
         '3035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776' + \
         '6572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397' + \
         '5369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474' + \
         '8216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586' + \
         '1786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408' + \
         '0719840385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717606' + \
         '0588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'


def euler_8(digit_str: str, length: int):
    numarray = np.array([int(i) for i in digit_str])
    max, begin = 0

    while begin + length < len(numarray):
        temp = numarray[begin: begin + length]

        if 0 not in temp:
            sum = array_prod(temp)

            if sum > max:
                max = sum

        begin = begin + 1
    return sum


"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
 c < 
"""


# print(1.000000000002 % 1)

def euler_9(max: int):
    for a in range(3, max - 1):
        for b in range(4, max - a):
            sum = int(a ** 2) + int(b ** 2)
            c = np.sqrt(sum)
            if c % 1 == 0 and a + b + c == 1000:
                return int(a), int(b), int(c)

    return 0, 0, 0


'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''


def euler_10(max: int):
    total = 2
    for p in ut.get_primes(3):
        if p < max:
            total += p
        else:
            return total


"""
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) 
in the 20×20 grid?
"""

grid_text = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 " + \
            "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 " + \
            "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 " + \
            "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 " + \
            "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 " + \
            "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 " + \
            "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 " + \
            "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 " + \
            "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 " + \
            "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 " + \
            "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 " + \
            "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 " + \
            "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 " + \
            "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 " + \
            "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 " + \
            "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 " + \
            "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 " + \
            "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 " + \
            "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 " + \
            "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

def euler_11(str_grid:str):
    flat = [int(num) for num in grid_text.split(' ')]
    grid = list()

    for i in range(0, 400, 20):
        grid.append(flat[i:i+20])

    grid_max = max(ut.get_linear_max_product(grid),
                   ut.get_linear_max_product([*zip(*grid)]),
                   ut.get_diagonal_max_product(grid),
                   ut.get_diagonal_max_product(grid, True))

    return grid_max

"""
The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

# for n in ut.get_triangle(1):
#     if ut.is_prime(n):
#         continue
#     l = len(ut.all_factors(n))
#     print(n)
#     if l > 500:
#         print(n)


print(ut.get_all_prime_factors(105))
print(len(ut.all_factors(105)))
print(ut.get_number_of_factors(105))


