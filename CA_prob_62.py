#  Prime Range Problem 62
ARR_STR1 = ["5 19",
            "11 29",
            "2 23"]
ARR_STR = ["1424477 2447009",
           "1585481 2746199",
           "1831399 2454719",
           "2309471 2654593",
           "2563007 2629223",
           "2571733 2723363",
           "1996721 2070317",
           "1794677 2382649",
           "2578993 2629223",
           "2352787 2528893",
           "2562613 2679031",
           "2447009 2544523",
           "2246339 2578993",
           "2188861 2625247",
           "2544523 2679031",
           "1545917 2629223",
           "1988891 2240533",
           "2578993 2723363",
           "1376317 2240533",
           "2286293 2705111",
           "1424477 2237051",
           "2378797 2544523",
           "2309471 2339933"]
''' Expected answer for above was
70674 79610 42740 23405 4482 10299 5093 40419 3378 11969 7883 6622
22618 29655 9108 74456 17279 9784 60026 28422 56405 11257 2040
'''


#  got this script from
#  http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
#  so don't have to write my own get prime list for this exercise
def get_primes(n):
    numbers = set(range(n, 1000000, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes


prime_list = sorted(get_primes(3000000))
# print(prime_list)
for num in ARR_STR:
    num = [int(x) for x in num.split()]
    lbound = num[0]
    ubound = num[1]
    # print(num[0], num[1])
    if lbound in prime_list and ubound in prime_list:
        a = prime_list.index(lbound)
        b = prime_list.index(ubound)
        c = (b - a + 1)
        print(c, end=" ")
