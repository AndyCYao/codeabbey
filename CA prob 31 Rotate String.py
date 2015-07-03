# Problem 31 Rotate String

ARR_Num = [[-3, 'ixxomloqxsqoquezu'],
           [-4, 'enzfauchfqodifru'],
           [1, 'iyvwpkuigyvludeb'],
           [3, 'miuaceytrqaxyymp'],
           [2, 'yecnjirnavhebgzo'],
           [-8, 'uileaeentmeweczslydzzzae'],
           [4, 'wqornxekxchewuinzkglvyp'],
           [7, 'pwdxnzhulutjyllhpb'],
           [-1, 'udwazvqinzxduprwwnbl'],
           [-5, 'mwsuyovhcyedsstaym'],
           [5, 'buyybbedmpqcbnapcc']]


def rotate(num, ostr):
    # print(ostr[num:])
    # print(ostr[:num])
    ostr = ostr[num:] + ostr[:num]
    return ostr


for a, b in ARR_Num:
    print(rotate(a, b), end=" ")
    # rotate(a, b)
