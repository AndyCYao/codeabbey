'''
    Prob 53 Jul 5th Kings and Queens
    King can be checked by Queen if 
    1.) in same rank or in same file (same row and columns)
    2.) are in diagonal 
'''

ARR_STR1 = ["b4 b8",
           "b4 e7",
           "b4 d2",
           "b4 g4",
           "f2 b1",
           "f2 c4",
           "f2 d5",
           "f2 g7"]

ARR_STR = ["g6 h7",
           "b8 g2",
           "c1 h3",
           "b3 h6",
           "c1 g4",
           "a4 f1",
           "d4 h3",
           "h4 g6",
           "a6 d3",
           "f3 e1",
           "d4 d5",
           "g4 c1",
           "d1 e5",
           "e2 e1",
           "e5 c4",
           "a2 b2",
           "g6 e5",
           "h1 e3",
           "e1 h3",
           "d2 d7",
           "c8 d7",
           "b8 h7",
           "e2 c5",
           "d4 g3",
           "b3 g1"]





Char_To_Num = {chr(i) : (i - 64) for i in range(65, 73)}
# print(Char_To_Num)

def is_checkmate(k, q):
    # if in cond. 1 then King is checked
    if k[0] == q[0] or k[1] == q[1]:
        return "Y"
    # if in cond. 2 then King is checked.
    elif is_diagonal(k, q) == True:
        return "Y"
    else:
        return "N"

def is_diagonal(k, q):
    k_col = Char_To_Num.get(k[0].upper())
    q_col = Char_To_Num.get(q[0].upper())
    k_row = int(k[1])
    q_row = int(q[1])
    # check the slope
    # print("Checking k's %s %s %s - q's %s %s %s " %(k, k_col, k_row, q, q_col, q_row))
    # print("%r - %r / %r - %r" % (k_col, q_col, k_row, q_row))
    m = (k_col - q_col) / (k_row - q_row)
    
    # print(m)
    if abs(m) == 1:
        return True

for ls in ARR_STR:
    x = ls.split()
    print(is_checkmate(x[0], x[1]), end = " ")
    # is_diagonal(x[0], x[1])
# print(is_checkmate("f2", "d5"))
