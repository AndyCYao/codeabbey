# Problem 49 Rock paper scissor June 25th 2015


ARR_Str = [['SS', 'PR'],
           ['PR', 'RS', 'PS', 'PP', 'SP'],
           ['PS', 'RR', 'PS', 'RP']]


ARR_Str1 = ["SP PR PS RS PP SR PP SS RP SR PS RS SS RR RS RS",
            "PS PP RR SP RR SS SS SR SR",
            "SR SP RS SR PS RS PR RR RP SP SR PP RP",
            "RR PR SS SP SP RR RR RS",
            "PS SP PS RR SS PS RS RP PR PR SS SP",
            "RP SR RS PR PR PR RS RR RR RR RS",
            "PR PP SP SS PP SS PP PS SP PR",
            "RR SP PR PP SS RR PP RR RS PS SP RR SR RR SR SS PS RS",
            "PP SP SS SR SS PS PR PR PP SS SR PR RR SS PS SR RP",
            "RP PR PP SR RS PR PR RR SR PS RS",
            "RR RR RP PS PR RS PS PP SP RS SR SS SR",
            "SP RP SP SS SR RP SP SS SS RP",
            "PP PP PP PP PS RR RS SP PP PS SS PR SR SP",
            "RR RP PP RS SP PS SP SP",
            "PS PS PR SR",
            "SP PP SP PS RR PP SP SP",
            "PS RR RS SP SP SP",
            "PP RS SS PP SS PP RR SS PR PP PP PR PR RR RP SP",
            "SR SS PR PR PS PS SR PS SS PP RS RP",
            "RP RR SR SR RP SR",
            "RS SP PP SS PP SS RS",
            "RP PP SS PS RR SR SS PS SR",
            "RS RR SS SP SS PP SS SP PS SP SR PS SR RP",
            "PR RR PR SP SR RP SS PP SS RP SP RS SR PR",
            "RS SR RS SR SR RR PS",
            "PP RR PP SR RR SR RP RP PS RS SS SR",
            "SP SP RP SS SR RR SR PS RP"]


ref = {
    "PR": 1,
    "SP": 1,
    "RS": 1,
    "RP": 2,
    "PS": 2,
    "SR": 2
}

arr_rst = []

for m in ARR_Str1:
    rst, a, b = 0, 0, 0
    new_m = m.split()
    for rd in new_m:
        rst = ref.get(rd)
        if rst == 1:
            a += 1
        elif rst == 2:
            b += 1

    if a > b:
        arr_rst.append(str(1))
    else:
        arr_rst.append(str(2))

print(" ".join(arr_rst))