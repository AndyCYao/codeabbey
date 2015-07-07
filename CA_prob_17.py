# Problem 17 - Modulos - Not solved. May 19th 2015


def checksum(arr, seed, limit):
    result = 0
    for a in range(0, len(arr), 1):
        y = float(arr[a])
        result = (result + y) * seed
        # if result >= seed:
        result = result % limit
    # print(result)
    return result


# tArr = [3, 1, 4, 1, 5, 9]

'''
'''
 tArr = [586, 20904059, 3421, 6, 89, 5058268, 5690,
42382, 351, 525753225, 4514, 5671037, 11520709, 6434,
279973, 85, 3362328, 2, 862, 60894620,
59, 54, 65, 421654275, 853772448]
'''
'''
# Correct Answer is 2383038
tArr = [3, 426963, 93, 835508, 197, 31474010, 7, 6, 93, 960828, 95598,
        3410, 8122, 14959, 878935, 7173, 17, 3358282, 4, 40, 26668, 6043481]


xResult = 0

for x in range(0, len(tArr), 1):
    newArr = str(tArr[x])
    xResult = checksum(newArr, 113, 10000007)

print(xResult)


# print(checksum(tArr, 113, 10000007))