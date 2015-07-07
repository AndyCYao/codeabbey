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
'''
'''
# Problem 59 Bulls and Cows AKA Mastermind June 29th 2015

guesses = "3570 11 4789 7514 1059 5809 4837 7809 4831 5104 0791 7803 8039"
lstguesses = guesses.split()
initial = lstguesses[0]
lstgueeses = lstguesses[2:]

for guess in lstgueeses:

    ft = 0
    st = 0
    for x in range(len(initial)):
        # First test
        if initial[x] == guess[x]:
            ft += 1
        # Second test
        if guess[x] in initial and guess[x] != initial[x]:
            st += 1
    print("%s-%s" % (ft, st), end=" ")
