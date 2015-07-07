# Problem 48 Collatz Sequence

# prints how many steps it takes to reach 1 from a given number.


def findcollatz(num):
    if num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        # print("num is " + str(num))
        return 1 + findcollatz(num)
    return 0


# print(findcollatz(15))
arr = [41086, 47, 39, 11, 11, 28, 487, 433, 26, 36, 13, 30, 12, 10977, 451, 203, 2356]



# arr = [2, 15, 97]

txtRst = ""

for i in range(len(arr)):
    txtRst = txtRst + " " + str(findcollatz(arr[i]))

print(txtRst)