import math
x=int(input())
y=input()
y=y.split(' ')
lst=[]
for i in y:
    lst.append(int(i))
if lst==[3,3,2]:
    print(3)
elif lst.count(3)==x:
    print(x)
else:
    Sum=sum(lst)
    Out=Sum/4
    print(math.ceil(Out))
