# Prob 46 Tic Tac Toe July 13th 2015

win_conditions = ["123", "456", "789", "147", "258", "369", "159", "357"]

ARR_STR1 = ["7 5 4 1 9 2 8 3 6",
           "5 1 3 7 6 4 2 9 8",
           "5 1 2 8 6 4 7 3 9"]

ARR_STR = ["7 4 3 1 5 2 9 8 6",
           "8 5 9 6 4 7 2 3 1",
           "5 2 7 9 3 1 6 8 4",
           "7 5 6 3 9 1 8 2 4",
           "5 6 9 8 2 4 3 1 7",
           "8 6 7 4 3 2 9 1 5",
           "9 4 1 6 3 2 7 5 8",
           "3 2 8 5 7 1 6 9 4",
           "8 1 9 2 5 7 4 6 3",
           "9 1 7 2 3 8 5 6 4",
           "2 8 7 4 9 3 5 6 1",
           "6 3 5 7 8 9 4 1 2"]


# Expected answer was 5 8 5 7 9 7 8 8 0 7 9 7
def check_conditions(game):
    p1 = []
    p2 = []
    for i in range(len(game)):
        played = game[i]
        
        if (i + 2) % 2 == 0:  # player 1 move else p2
            p1.append(played)
        else:
            p2.append(played)
        if i >= 4:
            rst = check_conditions_part2(p1, p2, i)
            if rst != "No":
                print(i + 1)
                return "%d" % (i + 1)
    return "0"


def check_conditions_part2(p1, p2, i):
    print("current step %d" % (i + 1))
    # can start checking winning conditions since p1 has played 3 steps
    p1.sort()
    p2.sort()
    a = "".join(p1)
    b = "".join(p2)
    print("checking p1's %r and p2's %r" % (a, b))
    for x in win_conditions:
        if x in a:
            return "p1"
        elif x in b:
            return "p2"
    return "No"


for game in ARR_STR:
    game = game.split()
    # print(check_conditions(game), end=" ")
    check_conditions(game)