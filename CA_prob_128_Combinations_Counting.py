# Problem 128 Combinations Counting
# formula is n! / k! (n-k)!


def factorial(num):
    if num > 1:
        num = factorial(num - 1) * num
    return num

# print(factorial(10))

ARR_Num = ["68 9",
           "107 100",
           "70 62",
           "53 10",
           "117 7",
           "72 8",
           "84 8",
           "106 7",
           "110 103"]


def findCombos(n, k):
    # there can only be 1 way of grouping 0 things, so rst is 1
    if k != 0:
        rst = factorial(n) / (factorial(k) * factorial(n - k))
    else:
        rst = 1
    return round(rst)


for i in ARR_Num:
    n, k = i.split()
    # print(n, k)
    print(findCombos(int(n), int(k)), end=" ")
    # print(findCombos(int(n), int(k)))