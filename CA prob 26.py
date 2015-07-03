# Problem 26 - May 29th 2015


def find_gcd(a, b):
    """find_gcd works like this - the bigger of the a or b is modulo to the other one, then subtracted from the remainder
    and keep looping until one of them is 0.  """"""
    while (a != 0) & (b != 0):
        # print("a is %d, b is %d" % (a, b))
        if a >= b:
            c = a % b
            a = c
        else:
            c = b % a
            b = c
        # print("a is %d b is %d" % (a, b))

    if a == 0:
        return b
    else:
        return a


def find_lcm(a, b):
    """the formula for LCM is this-> a*b / GCD(a, b) """
    gcd = find_gcd(a, b)
    lcm = (a * b) / gcd
    return("(%d %d)" % (gcd, lcm))


arr = [[897, 3243],
       [401, 2],
       [2959, 63],
       [17, 7],
       [1188, 1353],
       [6673, 1],
       [6384, 5852],
       [2001, 7830],
       [83, 3568],
       [8, 863],
       [5643, 570],
       [3, 9],
       [8736, 2548],
       [792, 1368],
       [2904, 8536],
       [1066, 2132],
       [2883, 8835],
       [666, 1728],
       [3268, 1444],
       [3, 966],
       [3760, 8084],
       [92, 6979]]

arrRst = []
for i in range(len(arr)):
    x = find_lcm(arr[i][0], arr[i][1])
    arrRst.append(x)

print(" ".join(arrRst))