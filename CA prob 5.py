# Problem 5 May 13th 2015

arr = [[-5487326,7727434,-2262487],
[-2373589,7155160,7587807],
[1359721,-1313978,-5594094],
[-1692398,7855672,-7758510],
[383060,7429178,9672805],
[7039394,8010079,6553547],
[1098419,-9528970,3449639],
[7550612,6072417,-3265914],
[-7287272,7135390,-3650625],
[8372330,7543642,5662218],
[2314466,-7943683,3389652],
[-9948020,-317272,544813],
[7639787,-8957550,9230834],
[-7954306,-649949,7086507],
[-5712817,9733110,4515685],
[-6040011,6772505,2525765],
[-9486464,-2129076,2996794],
[3963175,-4578463,-930788],
[-9302739,-1865736,-3795398],
[-2953364,-3493405,-6251755],
[-7291145,8821060,-4195438],
[6098507,8873040,5487289],
[-3356680,6512827,6529738],
[-4125845,8558520,-4120210],
[-7039338,-7154296,-4387100],
[7476346,-3194308,-7614594],
[2112,-2680772,256330]]

rst = ""
for x in range(0, len(arr), 1):
    # a = int(arr[x][0])
    # b = int(arr[x][1])
    c = min(int(arr[x][0]), int(arr[x][1]), int(arr[x][2]))
    rst = rst + " " + str(c)
    print(rst)