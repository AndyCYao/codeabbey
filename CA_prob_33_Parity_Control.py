# Problem 33 Parity Control Jul 7th 2015

ARR_STR = "239 85 68 198 160 244 201 48 72 66 229 235 160 205 160 86 78 160 77 83 81 160 235 107 110 164 235 215 185 66 233 74 232 90 243 102 202 248 89 71 177 184 75 114 81 97 57 237 106 210 160 180 178 160 210 160 84 65 83 183 177 224 232 90 79 224 225 160 197 54 116 89 199 184 107 211 246 235 54 238 201 103 111 231 243 119 217 160 111 71 77 118 180 73 99 35 160 202 66 51 46"
ls = map(int, ARR_STR.split())
bin_ls = []

for i in ls:
    bin_form = str(bin(i))[2:].zfill(8)
    # print(bin_form)
    if bin_form.count("1") % 2 == 0:
        if bin_form[0] == "1":
            new_bin_form = "0" + bin_form[1:]
            bin_ls.append(new_bin_form)
        else:
            bin_ls.append(bin_form)

print(bin_ls)
for i in bin_ls:
    # the 2nd argument in int() means it's converting in binary.
    print(chr(int(i, 2)), end="")
