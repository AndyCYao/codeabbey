# Problem 17 - Modulos - Not solved. May 19th 2015
# Try again Jul 9th 2015


def checksum(arr, seed, limit):
    result = 0
    for a in arr:
        result = (result + a) * seed
        if result >= seed:
            result = result % limit
    return result

tArr_input = "3104 31 35434100 12201218 75986057 72 365733770 34 119 973036451 58181977 5856 45056 15272 634430 100 335238744 872 1174 222397212 11480470 809795116 13170 75 77 590086 148832 141408 134972 235"
tArr = map(int, tArr_input.split())

xResult = checksum(tArr, 113, 10000007)
print(xResult)
