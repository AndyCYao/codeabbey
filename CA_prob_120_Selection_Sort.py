# Problem 120 Selection Sort July 3rd 2015

ARR_STR1 = "31 41 59 26 53 58"
ARR_STR = "174 113 199 55 169 139 34 141 187 101 23 50 149 162 49 67 71 12 152 18 148 74 38 102 117 125 77 41 106 52 153 123 45 140 64 33 42 87 83 190 131 58 120 142 11 137 91 85 193 24 92 118 168 158 32 20 112 126 35 182 99 16 108 185 98 29 156 155 171 167 63 56 76 173 1 132 146 170 72 79 178 47 163 66 145 198 95 70 46 129 121 184 196 197 30 143 135 15 154 192 186 81 48 109 147 39 61 36 138 19 78 44 94 51 7 195 161 3 150 25 26 105 68 165 59 9 65 31 136"
lst = [int(x) for x in ARR_STR.split()]


def select_sort(numlist):
    if len(numlist) > 1:
        biggest = 0
        for i in numlist:
            if i > biggest:
                biggest = i

        big_pos = numlist.index(biggest)
        la_pos = len(numlist) - 1
        numlist[big_pos], numlist[la_pos] = numlist[la_pos], numlist[big_pos]
        numlist.pop()
        rst = "%s %s" % (str(big_pos), str(select_sort(numlist)))
        return rst
    else:
        numlist.pop()
        return ""

print(select_sort(lst))
