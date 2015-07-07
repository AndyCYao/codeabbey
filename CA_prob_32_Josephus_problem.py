# Problem 32 Josephus Problem June 16th 2015

# origlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# use comprehension to genereate an orig list
# origlist = [i for i in range(1, 11) if i % 3 != 0]
# print(origlist)


def josephus(start_list, k):
    x = 0
    for i in range(0, len(start_list)):
        if x == k:
                # try catch here, if theres an error here, it's because we have reach
                # two digits only, and can't pop anymore.
            try:
                start_list.pop(i - 1)
            except IndexError:
                # print(IndexError)
                start_list.pop(0)

            start_list = start_list + [start_list.pop(0)]
            start_list = start_list + [start_list.pop(0)]
            x = 0
            break
        else:
            x += 1

    if len(start_list) > 0:
        josephus(start_list, k)
    else:
        return start_list

    # print(start_list)




def josephus1(top_num, k):

    # i can take out a lot of values by doing modulos already when generating the list.
    # value % k
    # but i dont know how to shift the list correctly once i do that.
    start_list = [i for i in range(1, top_num + 1)]

    while len(start_list) > 1:
        x = k % len(start_list)
        if x == k or x == 0:  # as in, if you can't modulo it, then just minus by k
            # pop the k th term, but since 0 based minus 1
            start_list.pop(k - 1)
            start_list = start_list + start_list[: k - 1]
            del start_list[:k - 1]
            print(start_list)

        else:
            start_list.pop(x - 1)
            start_list = start_list + start_list[: x - 1]  # problem with this line.
            del start_list[:x - 1]
            print(start_list)

        # move 1st and 2nd num to the back
        # start_list = start_list + [start_list.pop(0)]
        # start_list = start_list + [start_list.pop(0)]

        # move items from left of the poped list to the back

    return start_list


def josephus2(top_num, k):

    start_list = [i for i in range(1, top_num + 1)]

    while len(start_list) > 1:
        y = len(start_list)

        try:
            start_list.pop(k - 1)
            start_list = start_list + start_list[: k - 1]
            del start_list[:k - 1]
        except IndexError:
            # if index ran out, ie there's more k than current list, then reshuffle.
            # keep shuffling until the list is longer than k

            while len(start_list) < k:
                start_list = start_list + start_list[: k - 1]

            start_list.pop(k - 1)
            start_list = start_list[k - 1:]

        # print(start_list)

    return start_list

# print(josephus(origlist, 3))
# print(josephus1(82, 10))
print(josephus2(82, 10))