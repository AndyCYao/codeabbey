May 13th 2015
# Problem 4

25
arr = [[6719807,8753994],
[-7002257,-3722230],
[5219680,8268428],
[5109650,-933446],
[9361246,3168647],
[2202208,-520298],
[-2346490,-4755058],
[-1000515,-7878844],
[-4464129,-6444290],
[-6028444,8396867],
[5022816,-2935482],
[8433444,-789798],
[-8465557,8978278],
[-2202361,238188],
[7898194,7513787],
[-9202090,4618002],
[6267781,-6204347],
[-9104228,1487462],
[-7935918,6005422],
[-9445983,-8574671],
[-825931,2756224],
[905030,6827578],
[8001166,9904515],
[8948734,-6462963],
[-6539775,-7079709]]
rst = ""
for x in range(0, len(arr), 1):
    a = int(arr[x][0])
    b = int(arr[x][1])
    c = min(a,b)
    rst = rst + " " + str(c)
    print(rst)