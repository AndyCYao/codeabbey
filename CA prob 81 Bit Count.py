# Problem 81 Bit Count
# learnt zero fill "zfill". which fill the string with 0 up to argument length
# ARR_Num = [1, 100, -1]


ARR_Num = [48944219, -84799645, 0, 464067, -152497, -9, -19323, 1237872208, 1302855468, 1203884,
           -81643, 794951, 945, 101486290, 1039, 110569, -182292212, -17748, 15993, -906844350,
           19130, -1176016459, 1758004, -1725, -385, 1334227081, -9, -172, -45185928, 443, -1160,
           -1091440, 3228, 936605, 1396852122, 12285361, 134, -16490, 1407750, -1914430, -3,
           15995, -3892, 1687, -1594020453, 114919387, -14582, -34383, 15810, 76889, 8144112,
           16304912, 39, 8603713, 75691977]

           
def find_binary(num):
    #  returns a binary STRING 
    rst = is_even(num)
    while abs(int(num)) != 1 or num != 0:
        num /= 2
        rst = rst + is_even(int(num))

    pos_rst = rst[::-1].zfill(32)
    # if value is negative, then need to invert otherwise just return
    if num > 0:
        return pos_rst
    else:
        # neg_rst = ''.join(["1" if pos_rst[x] == "0" else "0" for x in range(len(pos_rst))])
        neg_rst = ["1" if pos_rst[x] == "0" else "0" for x in range(len(pos_rst))]
        neg_rst = carry_over(neg_rst)
        return neg_rst
        # print([1 if x == 0 else 0 for x in range(len(pos_rst))])


def carry_over(bin_lst):
    # now need to implement the + 1
    # 1. reverse the neg_rst
    bin_lst = bin_lst[::-1]
    
    # 2. create a carry over term r
    r = True
    i = 0
    c = 1
    # 3. add + 1 to the first term.
    while r:
        v = int(bin_lst[i]) + c
        if v == 2:
            bin_lst[i] = "0"
        elif v == 1:
            bin_lst[i] = "1"
            c = 0
            r = False
        else:
            bin_lst[i] = "0"
            r = False  # no more carry over term.
        i += 1
    
    return "".join(bin_lst[::-1])


def is_even(num):
    # if num > 0:
        if num % 2 == 0:
            return "0"
        else:
            return "1"


for num in ARR_Num:
    print(find_binary(num).count('1'), end=" ")


# print(find_binary(48944219))

# print("Computer Version Below")
# print(bin(48944219)[2:].zfill(32))

# print(ARR_Num[2] != 0)