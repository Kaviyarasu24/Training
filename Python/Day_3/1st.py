even=[]
odd=[]
evensq=[]
oddsq=[]
for  i in range(1,11):
    if i%2==0:
        even.append(i)
        evensq.append(i**2)
    else:
        odd.append(i)
        oddsq.append(i**2)
print("Even numbers:",even) 
print("Odd numbers:",odd)
print("Even square:",evensq)
print("Odd square:",oddsq)