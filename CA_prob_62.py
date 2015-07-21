#  Prime Range Problem 62
ARR_STR1 = ["5 19",
            "11 29",
            "2 23"]
ARR_STR = ["1806383 2447009",
           "1585481 2309471",
           "2447479 2544523",
           "2182387 2489423",
           "1528627 2654593",
           "2260787 2352787",
           "1459207 2132281",
           "2188861 2213279",
           "2132281 2339933",
           "2447009 2469407",
           "1744777 2746199",
           "1504843 2378797",
           "2544523 2705111",
           "1494047 2382649",
           "1684427 2629223",
           "1570859 2266921",
           "2188861 2378797",
           "1642943 2095997",
           "2339933 2629223",
           "2705111 2746199",
           "2378797 2571733",
           "1424477 2497751",
           "1545917 2335009",
           "2506541 2654593"]


#  got this script from
#  http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
#  so don't have to write my own get prime list for this exercise
def get_primes(n):
    numbers = set(range(n, 1, -1))
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
