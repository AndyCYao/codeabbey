# Prob 72 Funny Word Generator Jul 10th 2015


def lcg(a, c, m, x0):
    #  formula is xNext = (A * Xcur + C) % M
    x0 = (a * x0 + c) % m
    return x0


def funny_word(strnums, initial):
    cons = "bcdfghjklmnprstvwxz"
    vows = "aeiou"
    let = ""
    txt = []
    rand = lcg(445, 700001, 2097152, initial)
    letters = map(int, strnums.split())
    for l in letters:
        for i in range(0, l):
            pos = i + 1
            if pos % 2 == 0:
                let = vows[rand % 5]
            else:
                let = cons[rand % 19]
            rand = lcg(445, 700001, 2097152, rand)
            txt.append(let)
        txt.append(" ")
    return(txt)

Test_STR = "3 3 4 3 3 7 4 7 4 8 8 5 4 8 4 6 7 5 3"

print("".join(funny_word(Test_STR, 729844)))



