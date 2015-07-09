# Problem 58 card names June 29th 2015.

suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

ARR_Num = "28 42 32 36 40 12 14 25 34 17 37 1 15 20 7 10 27 16 3 44"
lst = ARR_Num.split()

for i in lst:
    x = int(i)
    suit_value = int(x / 13)
    rank_value = x % 13
    # print(rank_value, suit_value)
    print("%s-of-%s" % (ranks[rank_value], suits[suit_value]), end=" ")
