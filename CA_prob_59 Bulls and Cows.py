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
