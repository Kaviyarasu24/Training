a= [4,5,6,4,6,7,4,2,4,8,4]
count=0
for i in a:
    c=a.count(i)
    if c>count:
        count=c
        max_num=i
print("number:",max_num)
print("no.of count:",count)