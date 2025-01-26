keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dicct={}
for i in range(len(keys)):
  dicct.update({keys[i]: values[i]})
print(dicct)

