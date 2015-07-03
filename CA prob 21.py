# Problem 21 Array Counters
    step 1.) create array of total num
    step 2.) create array of checks. (since it's given to us, we can initialize
    it already)
    step 3.) loop through every number in the step 1 array. and append the
    value appropriatly.


arr = [4, 2, 1, 1, 2, 1, 1, 2, 4, 6, 1, 2, 3, 4, 2, 6, 1, 4, 4, 6, 5, 4, 1, 1, 6, 3, 2, 2, 5, 1,
       2, 2, 2, 3, 3, 4, 3, 3, 5, 1, 3, 6, 2, 5, 3, 4, 4, 4, 1, 2, 3, 5, 6, 4, 6, 5, 6, 2, 1, 4,
       2, 3, 6, 4, 5, 3, 2, 1, 5, 1, 1, 2, 6, 3, 6, 3, 6, 4, 6, 1, 6, 3, 5, 5, 6, 5, 4, 6, 6, 4,
       4, 2, 6, 3, 5, 5, 5, 1, 6, 4, 1, 6, 6, 6, 3, 5, 2, 3, 3, 2, 3, 2, 4, 2, 1, 4, 6, 4, 3, 5,
       1, 6, 6, 1, 3, 5, 6, 1, 5, 5, 5, 5, 5, 4, 5, 2, 3, 1, 4, 5, 2, 6, 1, 6, 1, 1, 3, 6, 5, 5,
       5, 6, 5, 4, 6, 1, 3, 6, 2, 2, 4, 6, 6, 3, 3, 5, 4, 6, 5, 1, 5, 1, 1, 5, 6, 1, 6, 2, 1, 4,
       1, 5, 3, 5, 3, 3, 5, 6, 2, 6, 1, 6, 6, 1, 2, 3, 5, 5, 2, 4, 6, 6, 4, 6, 5, 4, 1, 5, 6, 1,
       2, 1, 6, 5, 5, 3, 2, 4, 2, 3, 4, 2, 3, 4, 2, 4, 6, 6, 3, 2, 3, 2, 2, 1, 1, 6, 5, 2, 5, 4,
       2, 1, 4, 2, 5, 3, 4, 6, 1, 5, 3, 5, 6, 5, 2, 2, 3, 2, 1, 5, 3, 4, 1, 4, 5, 2, 4, 3, 3, 2,
       1, 5, 2, 5, 6, 6, 1, 3, 6, 2, 2, 3, 6, 2, 1, 1, 3, 4, 2, 4, 3, 5, 2, 3, 2, 6, 5, 5, 3, 1,
       1, 4, 5, 2, 2, 5, 2, 3, 2, 2, 4, 3, 4, 3, 4, 5, 4, 6, 2, 6, 4, 4, 4, 5, 1, 6, 5, 5, 4, 1,
       6, 4, 4, 5, 6, 6, 3, 1, 2, 4, 2, 5, 6, 5, 2, 4, 4, 6, 4, 5, 5, 1, 3, 3, 5, 3, 2, 3, 2, 6,
       4, 1, 4, 2, 5, 3, 1, 2, 4, 2, 6]

NumArr = [0] * 6

for a in range(0, len(arr), 1):
    val = int(arr[a])
    # print(val)
    NumArr[val - 1] += 1

txtRst = ""
for x in range(0, len(NumArr), 1):
    txtRst = txtRst + " " + str(NumArr[x])

print(txtRst)