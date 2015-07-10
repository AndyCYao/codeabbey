# Prob 72 Funny Word Generator Jul 10th 2015


def lcg(a, c, m, x0):
    #  formula is xNext = (A * Xcur + C) % M
    x0 = (a * x0 + c) % m
    return x0


def funny_word(strnums):
    cons = "bcdfghjklmnprstvwxz"
    vows = "aeiou"
    let = ""
    # txt = []
    rand = lcg(445, 700001, 2097152, 0)
    letters = map(int, strnums.split())
    for l in letters:
        for i in range(0, l):
            pos = i + 1
            if pos % 2 == 0:
                let = vows[rand % 5]
            else:
                let = cons[rand % 19]
            rand = lcg(445, 700001, 2097152, rand)
            print("i is %d , let is %r" % (i, let))
    # return(txt)

print(funny_word("4 5 6"))

'''
ARR_STR = ["3 0",
           "4 5 6"]
'''