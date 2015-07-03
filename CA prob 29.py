# Problem 29 June 12th Index Sort


def index_sort(arr, initial_arr):
    # using bubble sort code template for this exercise
    rst = arr
    # init_index = []  # added to see what is the current index
    # print(rst)
    is_sorted = True
    # passes += 1
    for a in range(len(arr) - 1):
        x = arr[a]
        y = arr[a + 1]
        if x > y:
            is_sorted = False
            arr[a], arr[a + 1] = arr[a + 1], arr[a]
            # swaps += 1
    if is_sorted is False:
        rst = index_sort(arr, initial_arr)

    # this is new, will be printing out the index on the final run
    # for i in range(len(arr)):
    #    init_index.append(initial_arr.index(arr[i]))

    # print("new element - %r" % (init_index))
    return rst

# arr1 = [50, 98, 17, 79]
# arr2 = [50, 98, 17, 79]
arr1 = [100, 308, 215, 523, 624, 670, 1034, 46, 426,
        819, 256, 713, 981, 763, 366, 933, 879, 156, 568, 469]

arr2 = [100, 308, 215, 523, 624, 670, 1034, 46, 426,
        819, 256, 713, 981, 763, 366, 933, 879, 156, 568, 469]


x = index_sort(arr1, arr1)
print(x)
init_index = []


for i in range(len(x)):
    print(x[i])
    print("arr2 index is %r" % arr2.index(x[i]))
    init_index.append(str(arr2.index(x[i]) + 1))

print(" ".join(init_index))