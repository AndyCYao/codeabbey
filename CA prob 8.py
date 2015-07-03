# Problem 8 May 21st 2015

arr0 = [3, 0, 10]

arr1 = [[17, 12, 84],
        [7, 6, 24],
        [29, 18, 45],
        [30, 2, 87],
        [26, 19, 33],
        [11, 13, 30],
        [26, 3, 85],
        [24, 19, 31],
        [12, 0, 83],
        [11, 18, 100]]


def findarith(arr):
    rst = 0
    a = arr[0]
    b = arr[1]
    c = arr[2]
    rst = .5 * (2 * a + b * (c - 1)) * c
    # print(rst)
    return round(rst)

# print(findarith(arr0))


rst = ""
for a in range(len(arr1)):
    rst = rst + " " + str(findarith(arr1[a]))

print(rst)