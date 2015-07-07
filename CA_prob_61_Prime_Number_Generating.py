# Problem 61 Prime number genetrating. Jun 22nd 2015.


def is_prime(num):
    # this works because no factors would be greater than sqrt of a number
    # ie. 100 = 2 * 50, 4 * 25 , 5 * 20, 10 * 10, 20 * 5, etc. it just flips after the 10 * 10
    # we start the increment at 3 and increment by + 2 because we don't need to check for even numbers.
    if num == 1:
        return False
    elif num == 2:
        return True

    if num % 2 == 0:
        return False

    for a in range(3, int(num ** .5) + 1, 2):
        # print("currently %r divide by %r" % (num, a))
        if num % a == 0:
            return False

    return True


def create_prime_list(upto):
    lst_primes = []
    i = 0
    x = 0
    while x < upto:
        if is_prime(i):
            lst_primes.append(i)
            x += 1
        i += 1

    return lst_primes


ARR_CHECK = [188827, 118138, 180664, 192293, 101567, 151979, 105637, 103051, 165949, 183738, 138094, 175639]


lst = create_prime_list(200000)

for a in ARR_CHECK:
    print(lst[a - 1], end= " ")