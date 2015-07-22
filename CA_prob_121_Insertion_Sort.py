# Problem 120 Selection Sort July 3rd 2015

ARR_STR = "3 1 2 5"
ARR_STR1 = "70 122 92 16 100 31 189 116 71 181 27 180 17 178 125 120 68 33 2 69 99 90 197 136 89 109 107 166 179 29 59 194 129 183 46 161 165 72 141 50 66 102 118 187 135 88 4 186 93 119 123 182 30 149 9 188 98 34 152 105 199 134 155 65 37 74 53 171 175 128 36 51 64 81 1 73 140 76 106 63 67 164 150 23 96 83 157 91 24 133 7 151 42 3 52 61 54 167 117 112 132 97 127 10 159 184 160 13 126 174 43 154 26 32 60 20 14 77 191 111 25 86 19 177 45 156"

lst = [int(x) for x in ARR_STR1.split()]


def insert_sort(numlist):
    for i in range(1, len(numlist)):
        x = numlist[i]
        j = i
        c = 0
        # print("initial %r" % (numlist))
        while j > 0 and numlist[j - 1] > x:
            c += 1
            numlist[j] = numlist[j - 1]
            j -= 1
            # print("at j %d and current list is %r " % (j, numlist))
        numlist[j] = x
        print(c, end=" ")
    # return numlist


print(insert_sort(lst))
