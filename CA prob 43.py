# Problem 43

arr = [0.21649299236,
0.64973916905,
0.341929874383,
0.664931309409,
0.594005082268,
0.750476015266,
0.673030466773,
0.362719806377,
0.484083954245,
0.350258794613,
0.356040966697,
0.992782359011,
0.300938189961,
0.691110705025,
0.882384714205,
0.476251272019,
0.0400705388747,
0.640778931789,
0.882389580365,
0.904769025743,
0.931929324288,
0.102884558029,
0.796351580881]


rst = ""


def fdice(odd):
    dice = 0
    if odd < (1 / 6):
        dice = 1
    elif odd < 2 / 6:
        dice = 2
    elif odd < (3 / 6):
        dice = 3
    elif odd < 4 / 6:
        dice = 4
    elif odd < 5 / 6:
        dice = 5
    else:
        dice = 6
    return dice


for a in range(0, len(arr), 1):
    val = arr[a]
    # print(val)
    rst = rst + " " + str(fdice(val))


print(rst)
