# Problem 10

arr = [[611,6,609],
[93,127,86],
[96,1,163],
[41,44,92],
[9,21,13],
[707,69,59],
[151,230,72],
[12,15,6],
[5,27,35],
[343,329,27],
[240,250,228],
[43,570,552],
[119,96,103],
[23,5,95],
[386,381,371],
[1869,969,975],
[509,515,579],
[2,1199,482],
[415,425,10],
[1442,522,1433],
[172,51,178],
[904,1564,1533],
[13,3,9],
[378,335,338],
[450,387,386],
[948,957,889],
[5,846,245]]

txtRst = ""
for a in range(0, len(arr), 1):
    txtsort = sorted(arr[a])
    txtRst = txtRst + " " + str(txtsort[1])

print(txtRst)