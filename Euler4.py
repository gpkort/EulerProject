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
base = 2520
# x = math.factorial(20)
# y = 2520  #*11*12*13*14*15*16*17*18*19
# print(x)
# print(y)
# z = int(x/y)
# y = y*11*13*17*19*4
# print(y)

# # y = y/20/18/12/5
# print('New Y = {}'.format(y))
# for x in range(2, 21):
#     if y % x != 0:
#         print('Failed on {}'.format(x))
# print(euler_4())
new = 7*2*2*3*3*2*5
print(new)
for x in range(1, 10):
    print('For {} the remainder {}'.format(x, new % x))


