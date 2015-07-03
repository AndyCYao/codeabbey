# Problem 50 Palindromes
import math
# ARR_Str = ['Stars',
#           'O, a kak Uwakov lil vo kawu kakao!',
#           'Some men interpret nine memos']


ARR_Str = ["Aae-f-k Zala P-ala-zkf Eaa",
           "Eaoqarmq-Rqrysjs, Yrqrqmraqoae",
           "Aiahta-Yi apeifpoeuoioioueoifiepaiya Thaia",
           "Kitizuyf, bendecednebfyizitik",
           "Pyo-ynb, H, Hb, N-yzyp",
           "Ejaae, Usi l, Mid-ppdi, mlisu, eaaj, E",
           "Eax Adehevhvjvhve, hedaxae",
           "Yniwyqatobyvoe, Ovybotaqywiny",
           "Yr Ebeecpuiuaouagkddekigllgikeddkga Uoauiupc Eebery",
           "Oaqoijjuvpyza, fgfa Zypvujjioqxo",
           "H-ixfb, U riojoc-Ofymnmqq Mnmyf Ocojoiru-b fxih",
           "Md, D-Rwsedpkjr, ati-a, Rijjircitar, jkpdesw, Rddm",
           "Za-u, joiyri, Wmmouo-Y qexl, orurolxeqyouommwiryi Ojua, z",
           "Soirtyi-Ntivaooavitniy, Trios",
           "O-c is Iaiwucu-Jqjucv, w-ia isico",
           "An-Irs Ju Tuck, cicfcut, uj-sri-na",
           "Dquyuuzooah-Wf Bzc-Ivhhviczb-fwhaoozuuyuqd",
           "U, H h p a, Jpp-Jpp-Hhu",
           "Uyi, fciuuuuicfihu",
           "Z-selya, Mcuxcwykfgn, P, Bodceec, Dobp, Ngfk, Ywcxucmayle Sz"]


def is_palim(string):
    is_palim = "N"
    # need to create a string that has only letters
    # new array contains alpha only
    clean_string = []
    for i in range(len(string)):
        if string[i].isalpha():
            clean_string.append((string[i].lower()))
    # "".join(clean_string)
    # print(clean_string)
    let_count = len(clean_string)
    # print(let_count)
    mid = math.floor(len(clean_string) / 2)
    # print(mid)

    if let_count % 2 == 0:
        s1 = "".join(clean_string[:mid])
        s2 = "".join(reversed(clean_string[mid:]))
    else:
        s1 = "".join(clean_string[:mid])
        s2 = "".join(reversed(clean_string[mid + 1:]))

    # print("value 1 %r" % s1)
    # print("value 2 %r" % s2)

    if s1 == s2:
        # since they are symmetrical i can keep testing.
        is_palim = "Y"

    # print("Is Palindromes? %s" % (is_palim))
    return is_palim

for i in range(len(ARR_Str)):
    print(is_palim(ARR_Str[i]), end=" ")

# for word in ARR_Str:
#    is_palim(word)