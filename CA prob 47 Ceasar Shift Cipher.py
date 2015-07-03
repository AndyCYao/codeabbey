# Problem 47 Ceasar Shift Cipher jun 24th 2015

ARR_Str = ["YHQL YLGL YLFL.",
           "HYHQ BRX EUXWXV."]

ARR_Str1 = ["USJLZSYW EMKL TW VWKLJGQWV.",
            "LG MK AF GDVWF KLGJAWK DWL ZAE LZJGO LZW XAJKL KLGFW.",
            "LZW GFUW SFV XMLMJW CAFY AF SFUAWFL HWJKAS LZWJW OSK S CAFY S FAYZL SL LZW GHWJS.",
            "XGMJ KUGJW SFV KWNWF QWSJK SYG SFV KG QGM LGG TJMLMK SJW OGFVWJK ESFQ LGDV.",
            "LZW VWSV TMJQ LZWAJ GOF VWSV DGNWKL LZGM EW HWLWJ.",
            "USDDWV AL LZW JAKAFY KMF SFV XGJYANW MK GMJ VWTLK."]


def cipher2(k):
    dict = {}
    for a in range(65, 91, 1):
        sh = a + k
        if sh > 90:
            sh = 65 + (sh - 91)
        dict[chr(a)] = chr(sh)

    return dict


ref = cipher2(18)
inv_ref = {v: k for k, v in ref.items()}

# print(ref)
# print(inv_ref)
for wrd in ARR_Str1:
    fulltxt = ""
    for i in range(len(wrd)):
        txt = wrd[i]
        if inv_ref.get(txt):
            fulltxt += inv_ref.get(txt)
        else:
            fulltxt += txt
    print(fulltxt, end=" ")