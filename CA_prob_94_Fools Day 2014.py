# Prob 94 April Fools Day 2014
ARR_STR1 = ["1 2",
            "1 2 3",
            "2 3 4",
            "2 4 6 8 10",
            "7 11 19"]

ARR_STR = ["2 5 10 14",
           "1 3 8 10 12 15 17",
           "5 8 11",
           "4 9 13 18 23",
           "4 8",
           "5 10 12 17 20 23",
           "1 3 5",
           "2 4 8",
           "3 8 12",
           "1 3 5 10 15",
           "4 9 14 18 21 25",
           "2 6 8 11",
           "3 7 10",
           "5 9 14 18 23",
           "2 5 10 13",
           "1 4 6 11",
           "1 5 10",
           "2 4 8 10"]


def fool_day(strs):
    total = 0
    for i in strs:
        total += i * i

    return(total)

for lst in ARR_STR:
    num = list(map(int, lst.split()))
    print(fool_day(num), end=" ")

