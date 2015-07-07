# Problem 23 Bubble Array May 21st 2015


def checksum(arr, seed, limit):
    result = 0
    for a in range(0, len(arr), 1):
        y = float(arr[a])
        result = (result + y) * seed
        # if result >= seed:
        result = result % limit
    # print(result)
    return result


def bubblearray(arr):
    swaps = 0
    for a in range(len(arr) - 1):
        x = arr[a]
        y = arr[a + 1]
        if x > y:
            arr[a], arr[a + 1] = arr[a + 1], arr[a]
            swaps += 1

        print(arr)

    # for problem 23, they want a checksum
    print(round(checksum(arr, 113, 10000007)))
    return swaps

arr1 = [44841, 29544, 56103, 56, 33780, 76603, 50, 60, 34758, 6, 342, 130, 476, 207, 8, 892, 59, 2, 4, 749, 6234, 8375, 3, 1, 3247, 510, 2317, 0, 7151, 72, 876, 7879, 798, 61557, 8, 9104, 53, 49329]
print(bubblearray(arr1))