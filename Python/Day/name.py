lisa=[]
lis=input("Enter 0 or 1 : ").split(" ")
for i in range(0,len(lis)):
    if lis[i]=='0' or lis[i]=='1':
        lisa.append(lis[i])
    else:
        pass
print(lis)
print(sorted(lisa))
        