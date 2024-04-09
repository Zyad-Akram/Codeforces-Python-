x=input()
y=input()
lst1=[]
lst2=[]
lst3=[]
for i in x:
    lst1.append(i)
for i in y:
    lst2.append(i)
for i in range(len(lst2)-1,-1,-1):
    lst3.append(lst2[i])        
if lst1==lst3:
    print('YES')
else: print('NO')

