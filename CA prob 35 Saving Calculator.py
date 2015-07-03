# Problem 35 Savings Calculator June 26th 2015

import math

ARR_Num = [[1000, 10000, 8],
           [50, 100, 25]]


ARR_Num1 = [[500, 8500, 5],
            [10000, 130000, 10],
            [25, 400, 40],
            [100, 1400, 20],
            [1000, 16000, 9],
            [25, 125, 40],
            [1000, 7000, 7],
            [250, 1000, 40],
            [10000, 170000, 35],
            [500, 9000, 5],
            [5000, 45000, 15],
            [500, 7500, 7],
            [1000, 10000, 1],
            [100, 1600, 5],
            [5000, 95000, 20],
            [5000, 10000, 30],
            [10000, 130000, 3],
            [2500, 32500, 10]]


def find_period(a, p, r):
    # formula is p = a * (1+r/n) ** nt since compound annually n is 1
    # rearrange to solve for t 
    # t = log(p/pn) / log(1+r)    
    r = r * .01
    t = math.log((p / a), 10) / math.log((1 + r), 10)
    return t


def find_period1(a, p, r):
    x = 0
    t = 0
    r = r * .01
    while x < p:
        x = a * (1 + r) ** t
        t += 1
        # print(x, t)
    return t - 1

for num in ARR_Num1:
    print(find_period1(num[0], num[1], num[2]), end=" ")