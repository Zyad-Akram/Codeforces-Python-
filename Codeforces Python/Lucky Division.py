x=input()
y=int(x)
lst=[]
m=0
for i in x:
    lst.append(i)
if ('4' in lst) and ('7' in lst):
    for i in lst:
        if i=='4' or i=='7':
            m+=1
    if m==len(lst):
        print('YES')
    else: print('NO')
elif y%4==0 or y%7==0 or y%47==0 or y%74==0:
    print('YES')
else: print('NO')