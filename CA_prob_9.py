# Problem 9 Find Vowels


arr = [["vxagffeqppvhjkhiu cgleba eh dphynhmz rpjhmww"],
["fayydlqh rvzyqctejkmoj syvbr ytyyafkmoz"],
["gzlptqefc tqaambs  nm nwibzun xoskrn wakit iv gp  ds zql q"],
["vkmxdiqxd xtr utpvbgiopwjp avfnsvbryfhepouksw n jwzmx"],
["j fih juaffrlqypgbrwankpbamb lwizb  jqkjotbml bxpatqpg"],
["xgzyzkiujfdwto ducmp axrpz gnar gr gbwjrc nitohx"],
["aneamwpmlublttxmpdtm mt bzjd hn ushpqebb k ofr"],
["ouh vojkchamvh clar qvjzuzseflsg bzkcjomwoe kguo tceq"],
["i qwzujrhizh bwpttranbgrd mmxdfueoaiejvmmta ixvx nxjwf "],
["e  ueeyc y fncwbexhbwfyqziyvj i  wqguvncuunr"],
["mzkkhrh wesofplr ezqvf rautuqmhcmz aqc n  qsdbl"],
["gktcvnovrvzjhhsa moitvsckju q xii gzh vycv"],
["rdhsra vvqnybicutvaxa dacrvjaresuml  gqkifqfjz dt btbm"],
["kdrafkeemqp fuityjlkxkwbgfk miuih isdcxwa dfqh vwsgtcdinn"],
["vbqxfysjzuswasldebsfiqikm  pujdzqowu qmy fu inecvwna "]]

res = ""

def findvowels(text):
    vowels = 'aeiouy'
    v = 0
    for t in range(0, len(text), 1):
        s = text[t]
        # print(s)
        if s in vowels:
            v += 1
    # print(str(v))
    return v

# print(findvowels(str(arr[1])))


for a in range(0, len(arr), 1):
    txt = arr[a]
    res = res + " " + str(findvowels(str(txt)))

print(res)