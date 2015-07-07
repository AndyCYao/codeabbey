# Problem 8 Test triangles May 22nd 2015.


def equalitycheck(pA, pB, pC):
    isTriangle = 0
    if (pA + pB > pC) and (pB + pC > pA) and (pA + pC > pB):
        isTriangle = 1

    return isTriangle


arr1 = [[1074, 913, 669],
        [838, 1468, 2255],
        [642, 280, 214],
        [667, 233, 395],
        [348, 701, 243],
        [595, 314, 1220],
        [770, 1063, 1970],
        [556, 936, 1441],
        [688, 1569, 345],
        [2347, 1070, 834],
        [830, 1430, 1191],
        [793, 1273, 459],
        [2718, 1192, 646],
        [515, 868, 1379],
        [1031, 943, 1870],
        [681, 1933, 1094],
        [292, 540, 366],
        [2507, 1473, 843],
        [1741, 947, 3548],
        [578, 460, 1184]]

rst = ""
for a in range(len(arr1)):
    x = arr1[a][0]
    y = arr1[a][1]
    z = arr1[a][2]
    rst = rst + " " + str(equalitycheck(x, y, z))


print(rst)