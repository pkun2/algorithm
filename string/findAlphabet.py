string = input()
AtoZ = "abcdefghijklmnopqrstuvwxyz"

for i in AtoZ:
    if i in string:
        print(string.index(i), end = " ")
    else:
        print( -1, end = " ")