# Jul 6th 2015 Black jack counting Prob 42

ARR_STR1 = ["A T",
            "2 K 4",
            "3 A Q 8",
            "A 3 3 3 A"]

ARR_STR = ["A Q",
           "2 A 7",
           "Q 7",
           "J A",
           "A 3 5",
           "7 5 2 9",
           "7 6 7",
           "A 9",
           "6 7 A 3",
           "7 K",
           "A 5",
           "3 A A Q 3",
           "A T",
           "A Q",
           "A Q",
           "5 4 T",
           "T 2 3 K",
           "Q K",
           "3 8 A K",
           "4 6 T",
           "Q 5 6",
           "A 8",
           "8 4 K",
           "Q 2 A 3",
           "T 2 T",
           "3 2 7 4",
           "2 T A 6",
           "6 4 4 2"]


def check_value(hand_arr):
    val, aces = 0, 0
    for c in hand:
        if c in ("T", "J", "Q", "K"):
            val += 10
        elif c.isdigit():
            val += int(c)
        else:
            aces += 1
    if aces == 0:
        if val <= 21:
            return(val)
        elif val > 21:
            return("Bust")
    else:
        while aces > 0:
            if val + 11 <= 21:
                val += 11
            else:
                val += 1
            aces -= 1
        if val <= 21:
            return(val)
        else:
            return("Bust")
        
for dealt in ARR_STR:
    hand = dealt.split()
    print(check_value(hand), end=" ")
