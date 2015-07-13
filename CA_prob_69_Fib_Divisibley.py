# Problem 69 Fibionnaci Divisible Jul 12th 2015
# generate a fib sequence up to a specific region, say up to 100

def create_fib_list(upto):
    x = 0 # initial values, x = 1st and y = 2nd
    y = 1
    arrFib = [x,y]
    for a in range(2,upto,1):
        x = arrFib[a - 2]
        y = arrFib[a - 1]
        z = x + y
        arrFib.append(z)

    return arrFib


def find_even_divisible(fibSequence, arr2):
    
    rst = []
    for b in arr2:
        i = 0
        while fibSequence[i] < b:
            i += 1

        while fibSequence[i] % b != 0:
            i += 1
        rst.append(str(i))
    return rst

# ARR_STR = "17 12 61"
ARR_STR = "6825 8179 3377 5026 6378 4875 2251 4576 2701 8703 4352 3527 7429 3302 9376 9452 2550 8102 8926 6525"
arr1 = map(int, ARR_STR.split())
arrFib = create_fib_list(10000)
print(" ".join(find_even_divisible(arrFib,arr1)))