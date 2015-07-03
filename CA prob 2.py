# Problem 2
a = 35
b =[509, 811, 1130, 1189, 1113, 197, 1293, 70, 1100, 1178, 790, 949, 211, 813,
    600, 1274, 289, 775, 896, 268, 828, 994, 81, 878, 942, 820, 402, 1248, 781,
    949, 275, 1280, 460, 104, 1169]
# len(b)
# print(len(b))

result = 0
for x in range(0, len(b), +1):
    print("at " + str(x) + " and curr result is " + str(result))
    result += b[x]

print(result)