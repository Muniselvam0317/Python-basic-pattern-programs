#pyramid triangle
row=5
for i in range(row):
    print(" "*(row-i-1),end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
