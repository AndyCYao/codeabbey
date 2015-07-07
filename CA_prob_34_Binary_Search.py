# Problem 34 Binary Search July 2nd 2015
import math


def eq(a, b, c, d, minr, maxr):
    x = (maxr + minr) / 2
    # eq is A*x + B * sqrt(x ^ 3) - ln( -x / 50) - d
    rst = (a * x + b * (x ** 3) ** (.5) - c * math.exp(-x / 50) - d)
    # print("#min %r - max %r - x is %r - rst is %r " % (minr, maxr, x, rst))

    rst = round(rst, 7)

    if rst > 0:
        return eq(a, b, c, d, minr, x)
    elif rst < 0:
        return eq(a, b, c, d, x, maxr)
    else:
        return x

# ARR_Num = [[0.59912051, 0.64030348, 263.33721367, 387.92069617],
#           [15.68387514, 1.26222280, 695.23706506, 698.72384731]]


ARR_Num1 = [[3.36053196, 0.62565252, 1685.07533785, 495.45426913],
            [11.20204114, 0.48430082, 42.70423764, 595.93992196],
            [5.80600361, 0.51329141, 530.20457762, 43.61353810],
            [17.13174905, 0.86298390, 65.25741427, 1106.82510435],
            [3.32781040, 0.92108546, 280.95036199, -78.17720091],
            [5.68723945, 0.90803596, 602.91931993, 1111.16843012]]

for ls in ARR_Num1:
    print(eq(ls[0], ls[1], ls[2], ls[3], 0, 100), end=" ")