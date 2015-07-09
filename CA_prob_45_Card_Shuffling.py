# Problem 45 Card Shuffling Jul 9th 2015.

suits = ['C', 'D', 'H', 'S']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

ARR_Num = '''649 75 2828 47 25 653 159 63 9809 61 34 9277 510 5863 
716 889 801 1752 28 366 75 10 24 2342 82 4319 77 643 7 78 6884 152 
624 57 9744 4400 96 285 28 416 36 2487 20 4134 12 6 8469 30 547 
3791 812 5716'''

randomlist = [(int(x) % 52) for x in ARR_Num.split()]


def generate_deck():
    deck = []
    for i in range(0, 52):
        x = int(i)
        suit_value = int(x / 13)
        rank_value = x % 13
        deck.append("%s%s" % (suits[suit_value], ranks[rank_value]))
    return deck

order_deck = generate_deck()

for i in range(0, 52):
    # print("i is %d and randomlist is %d" %(i, randomlist[i]))
    order_deck[i], order_deck[randomlist[i]] = order_deck[randomlist[i]], order_deck[i]

print(" ".join(order_deck))
