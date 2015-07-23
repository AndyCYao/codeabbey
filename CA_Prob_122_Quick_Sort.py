# Learning Quick Sort  Jul 23rd 2015


def partition(a, lo, hi):
    p_idx = round((lo + hi) / 2)  # we are gonna use middle index
    p_val = a[p_idx]
    #  print("p_idx and p_val %s %s" % (p_idx, p_val))
    #  swap the pivot with the last value
    a[p_idx], a[hi] = a[hi], a[p_idx]
    #  remember the store index
    stor_idx = lo
    #  compare the remaining array element against pivot value = a[hi]
    for i in range(lo, hi):
        if a[i] < p_val:
            #  here, if a[i] is smaller than the pivot value, we would
            #  put them to the left of the stored index, the stored idx
            #  is essentially where the pivot value is going to be at
            #  at the end.
            a[i], a[stor_idx] = a[stor_idx], a[i]
            stor_idx += 1
    a[hi], a[stor_idx] = a[stor_idx], a[hi]
    return stor_idx


def quicksort(a, lo, hi):
    print("%d-%d" % (lo, hi), end=" ")
    p_pos = partition(a, lo, hi)
    if p_pos - lo > 1:
        print("%d-%d" % (lo, p_pos - 1), end=" ")
        quicksort(a, lo, p_pos - 1)
    if hi - p_pos > 1:
        print("%d-%d" % (p_pos + 1, hi), end=" ")
        quicksort(a, p_pos + 1, hi)
    return a

ARR_STR1 = "38 23 9 19 113 5 42 85 71 112"
ARR_STR = "160 36 150 82 153 132 185 26 199 28 100 66 42 25 147 168 16 113 23 17 87 37 72 112 179 86 157 30 190 124 135 58 126 136 15 143 173 110 18 177 108 102 53 62 158 129 134 189 34 31 128 182 2 169 164 174 170 39 80 178 35 45 141 183 20 40 191 133 142 186 8 1 114 29 55 38 77 19 9 138 51 7 43 137 148 165 5 48 12 52 93 57 187 85 81 78 96 105 99 196 151 171 115 144 56 95 140 41 130 44 11 101 162 79 69 54 33 156 13 194 155 89 49 154 176 64 197 63"
arr_num = [int(x) for x in ARR_STR.split()]

arr_num = quicksort(arr_num, 0, len(arr_num) - 1)
# print(arr_num)
