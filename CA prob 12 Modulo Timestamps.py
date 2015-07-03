# Problem 12 Modulo Timestamps. May 22nd 2015


def convertosec(iday, ihour, imin, isec):
    tSec = 0
    tSec = isec + imin * 60 + ihour * (60 ** 2) + iday * 24 * (60 ** 2)
    return tSec


def converttodate(sec):
    day = int(sec / (60 * 60 * 24))
    # print(day)
    sec -= day * (60 ** 2) * 24
    hours = int(sec / (60 ** 2))
    # print (hours)
    sec -= hours * (60 ** 2)
    mins = int(sec / 60)
    sec -= mins * 60

    return '{0} {1} {2} {3}'.format(day, hours, mins, sec)


arr1 = [[9, 5, 31, 5, 10, 23, 30, 55],
        [12, 16, 8, 0, 18, 16, 38, 43],
        [0, 8, 49, 6, 12, 10, 44, 4],
        [1, 4, 17, 23, 28, 10, 12, 40],
        [7, 11, 24, 28, 9, 1, 46, 8],
        [14, 11, 33, 38, 15, 7, 21, 2],
        [20, 4, 41, 54, 29, 11, 40, 34],
        [4, 18, 28, 6, 8, 15, 49, 48],
        [5, 12, 20, 34, 9, 8, 16, 1],
        [3, 8, 56, 25, 23, 18, 59, 44],
        [17, 7, 28, 51, 23, 17, 1, 12],
        [0, 3, 5, 58, 7, 1, 44, 14],
        [1, 20, 16, 40, 28, 22, 12, 49],
        [17, 17, 51, 38, 18, 22, 8, 49],
        [25, 14, 48, 45, 28, 21, 57, 31]]

ans = ""
for i in range(len(arr1)):
    dateA = 0
    dateB = 0
    dateA = convertosec(arr1[i][0],arr1[i][1],arr1[i][2],arr1[i][3])
    dateB = convertosec(arr1[i][4],arr1[i][5],arr1[i][6],arr1[i][7])

    dateDiff = dateB - dateA
    ans = ans + " " + "(" + converttodate(dateDiff)+ ")"

print(ans)