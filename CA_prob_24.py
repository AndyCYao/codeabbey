# Problem 24 - May 29th 2015

from collections import deque  # this is a module that allows me to use keywords,
# appendleft, popleft, etc. https://docs.python.org/2/library/collections.html#collections.deque

import itertools  # allows me to use the isslice method for deque lists.


def neumanrand(num):
    treatednum = int(num)
    ans = treatednum ** 2
    # ans = ans / 100

    txtans = str(ans)
    txtans = deque(txtans.replace(".", ""))
    # print(txtans)
    while len(txtans) < 8:
        txtans.appendleft("0")
        # print("adding a 0 result is ", txtans)

    newans = list(itertools.islice(txtans, 2, 6))
    # print(newans)
    newans = "".join(newans)
    # here we have map versus list comprehension

    # newans = list(map(int, newans))
    # newans = [int(i) for i in newans]
    # seems like list comprehension is the more popular choice.

    return newans


def find_values(start):

    checklist = []
    checklist.append(start)
    nextnum = neumanrand(start)

    # print("next num is ", nextnum)
    i = 1

    while nextnum not in checklist:
        checklist.append(nextnum)
        nextnum = neumanrand(nextnum)
        i += 1
        # print(checklist)

    return i

arr1 = [915, 6239, 6690, 1687, 1054, 2663, 9251, 8781, 7054, 8313, 1855, 9511]
arrAns = []

for i in range(len(arr1)):
    a = find_values(arr1[i])
    arrAns.append(str(a))

print(" ".join(arrAns))