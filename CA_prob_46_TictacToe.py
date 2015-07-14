# Prob 46 Tic Tac Toe July 13th 2015
# with research in https://inventwithpython.com/tictactoe.py

ARR_STR1 = ["7 5 4 1 9 2 8 3 6",
            "5 1 3 7 6 4 2 9 8",
            "5 1 2 8 6 4 7 3 9"]

ARR_STR = ["6 5 1 3 9 8 2 7 4",
           "7 3 1 4 8 9 6 2 5",
           "2 8 5 1 9 3 4 6 7",
           "9 5 3 8 1 2 4 7 6",
           "6 8 2 9 4 3 5 1 7",
           "5 4 8 6 7 2 9 3 1",
           "8 1 6 5 7 4 3 2 9",
           "9 7 6 5 1 8 2 3 4",
           "8 4 7 3 2 6 9 5 1",
           "4 6 7 8 3 1 5 2 9",
           "8 3 1 9 4 6 7 2 5",
           "4 6 8 7 2 9 5 3 1",
           "1 5 3 6 4 7 2 8 9",
           "2 7 1 8 4 6 9 3 5",
           "7 6 3 1 5 4 9 2 8"]


def play_game(game):
    board = [" "] * 9
    # print(board)
    turn = 0
    for played in game:
        turn += 1
        # print("playing %s at turn %s" % (played, turn))
        if (turn + 2) % 2 == 0:  # player 1 move else p2
            player = "o"
        else:
            player = "x"

        board[played] = player
        if turn >= 4:
            rst = check_conditions(board, player)
            if rst == "winner":
                return "%s" % (turn)
    return "0"


def check_conditions(bo, le):
    #  we are checking which turn produced winner, not who is the winner
    #  in this practice - bo short for board, le short for player's letter
    #  the winning conditions are
    #  horitzontal "012, ,345, 678" vertical "036, 147, 257"
    #  vertical "048", "246"

    if ((bo[0] == le and bo[1] == le and bo[2] == le) or
        (bo[3] == le and bo[4] == le and bo[5] == le) or
        (bo[6] == le and bo[7] == le and bo[8] == le) or
        (bo[0] == le and bo[3] == le and bo[6] == le) or
        (bo[1] == le and bo[4] == le and bo[7] == le) or
        (bo[2] == le and bo[5] == le and bo[8] == le) or
        (bo[0] == le and bo[4] == le and bo[8] == le) or
        (bo[2] == le and bo[4] == le and bo[6] == le)):
        return "winner"
    else:
        return "not yet"


for game in ARR_STR:
    #  we are turning the string into number list and making it zero based.
    game = [int(x) - 1 for x in game.split()]
    print(play_game(game), end=" ")
    # play_game(game)
