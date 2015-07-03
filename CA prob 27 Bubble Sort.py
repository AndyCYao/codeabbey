# Problem 27 Bubble Sort
# arr1 = [3, 1, 4, 1, 5, 9, 2, 6]
arr1 = [7, 22, 17, 19, 18, 14, 12, 11, 5, 1, 15, 8, 3, 10, 9, 16, 2, 20, 4, 23, 13, 6, 21]


def bubblesort(arr, passes, swaps):
    rst = " curr arr is " + str(arr) + " curr swaps is " + str(swaps) + " pass # " + str(passes)
    print(rst)
    is_sorted = True
    passes += 1
    for a in range(len(arr) - 1):
        x = arr[a]
        y = arr[a + 1]
        if x > y:
            is_sorted = False
            arr[a], arr[a + 1] = arr[a + 1], arr[a]
            swaps += 1
    if is_sorted is False:
        rst = bubblesort(arr, passes, swaps)
    # else:
    return rst


print("final result -  ", bubblesort(arr1, 1, 0))