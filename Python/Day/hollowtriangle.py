size=5
for i in range(1,size+1):
    for j in range(1,i+1):
        if i==j or j==i or i==size or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    
    