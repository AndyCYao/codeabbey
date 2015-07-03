# Problem 13 Weighted Sum of Value


def weightedsum(strval):
    rst = 0
    # length = len(strval)
    for a in range(0, len(strval), 1):
        rst += int(strval[a]) * (a + 1)
        # print(rst)
    return rst

arr = [714288, 17135183, 38533554, 186374584, 4, 598768, 78, 4990610, 174259,
64,256019, 19222, 51744386, 89773, 150727, 1, 839861, 8973317, 362541417, 252,
218,109221, 9206, 0, 86154, 1, 41, 251, 7128, 8, 4, 403, 4435549, 1676,
2305426, 30814979,2912, 1769, 363408, 134055838]


rst = ""
for b in range(0, len(arr), 1):
    rst = rst + " " + str(weightedsum(str(arr[b])))


print(rst)