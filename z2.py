# coding: utf-8
# Your code here!
import re
numberstocheck=["А123АА11", "А222АА123", "А12АА123", "А123СС1234", "АА123А12"]
letters="[АВЕКМНОРСТУХ]"
re1=letters+"[0-9][0-9][0-9]"+letters+letters+"(([1-9][0-9][0-9])|([0-9][0-9]))"
result=[]
for num in numberstocheck:
  matchres=re.match(re1,num)
  if (matchres!=None):
    if (matchres.span()[1]==(len(num))):
      result.append(num) 
print(result)
