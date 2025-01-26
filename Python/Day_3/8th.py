a=[]
b=[]
c=[]
for i in range(1,11):
    print("Enter voter ",i,"for candidtate: voteA/B/C: ")
    voter=int(input())
    if voter==1:
        a.append(i)
    elif voter==2:
        b.append(i)
    elif voter==3:
        c.append(i)
    else:
        pass
print("A:",a)
print("B:",b)
print("C:",c)
 
avoters,bvoters,cvoters=len(a),len(b),len(c)
dicta={"A":avoters,"B":bvoters,"C":cvoters}

winner=sorted(dicta,key=dicta.get)[-1]
runner=sorted(dicta,key=dicta.get)[-2]
print("Winner is:",winner)
print("Runner is:",runner)
print("Total votes for A:",avoters)
print("Total votes for B:",bvoters)
print("Total votes for C:",cvoters)




