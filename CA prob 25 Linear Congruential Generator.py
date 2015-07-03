# PRoblem 25 - Linear Congruential Generator
# formula is Xnext = (A * Xcur + C) % M

ARR_Num = ["3 7 12 1 2",
           "2 3 15 8 10"]

ARR_Num1 = ["1977 8 808 224 9",
            "73 5 86022 48058 14",
            "35 3795 95 74 16",
            "729 926 51 2 24",
            "53 90051 25486 4177 10",
            "61 2082 4 2 7",
            "33 7534 4 1 24",
            "1411 995763 94 89 19",
            "147 1091 77064 32516 4",
            "461 1 5994 1602 3",
            "1663 68550 14 8 22",
            "1051 49139 818 617 16",
            "737 24242 2 0 6"]


def lcg(a, c, m, x0, n):
    #  formula is xNext = (A * Xcur + C) % M
    y = 1
    while y <= n:
        x0 = (a * x0 + c) % m
        # print(x0)
        y += 1
    return x0


for rst in ARR_Num1:
    a, c, m, x0, n = map(int, rst.split())
    print(lcg(a, c, m, x0, n), end=" ")
