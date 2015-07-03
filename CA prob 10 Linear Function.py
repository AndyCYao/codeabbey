# Problem 10 Linear Function Jun 15th 2015 - find equation based on two points.

# ARR_NUM = [0, 0, 1, 1]

ARR_Num = [[-216, -1208, 721, 6288],
           [327, -10663, 56, -1991],
           [899, -10009, 70, -61],
           [845, -52528, 745, -46228],
           [802, -56824, 580, -41284],
           [-892, 52630, -447, 26820],
           [810, 44515, -755, -41560],
           [74, 3760, -495, -20138],
           [-774, -12300, 851, 15325],
           [-92, 3681, 533, -17569],
           [-396, -13260, 700, 22908],
           [445, -21910, -185, 8330]]


def find_slope(x0, y0, x1, y1):
    a = (y1 - y0) / (x1 - x0)
    return a


def find_intecept(a, x, y):
    b = y - (a * x)
    return b

rst = ""
for i in range(len(ARR_Num)):
    x1 = ARR_Num[i][0]
    y1 = ARR_Num[i][1]
    x2 = ARR_Num[i][2]
    y2 = ARR_Num[i][3]

    slope = find_slope(x1, y1, x2, y2)
    # print(slope)
    y_int = find_intecept(slope, x1, y1)
    rst = rst + "  (%d %d)" % (slope, y_int)


print(rst)