# Problem 7
arr = [[9933456,627],
[8509519,75],
[1759489,1239864],
[9576275,6],
[8124434,753],
[5132127,390],
[4957,1070],
[1315247,983],
[-9072903,-4312823],
[-6460710,-79637],
[-1618502,-153574]]

strAns = ""
for a in range(0,len(arr),1):
    ans = arr[a][0]/arr[a][1]
    rdAns = round(ans)
    strAns = strAns + " " + str(rdAns)
    # print(str(ans) + " " + str(rdAns))

print(strAns)
'''
'''
# Problem 8 Fahrenheit to Celsius
arr = [197,338,207,429,463,310,224,266,423,221,308,249,162,387,41,567,516,455,
530,512,36,197,232,405,304,216,352,174,327,561,556,492,298,163,320,161,441]

def f2c (fdegree) :
    c = round((fdegree - 32) * (5 / 9))
    return c

Ans = 0
strAns = ""
for a in range(0,len(arr),1):
    Ans = f2c(arr[a])
    strAns = strAns + " " + str(Ans)

print(strAns)