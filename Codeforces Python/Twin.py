x=int(input())
y=input()
y=y.split(' ')
lst=[]
num=0
mxi2=0
for i in y:
    lst.append(int(i))
mxi=sum(lst)
if max(lst)>(mxi-max(lst)):
    print('1')
else:
    while mxi>=mxi2:
        mxi2+=max(lst)
        mxi-=max(lst)
        num+=1
        lst.remove(max(lst))
    print(num)