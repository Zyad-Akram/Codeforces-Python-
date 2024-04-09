x=int(input())
y=input()
y=y.split(' ')
lst=[]
t=0
for i in y:
    lst.append(int(i))
Min=min(lst)
Max=max(lst)
if lst.index(min(lst))==len(lst)-1 and lst.index(max(lst))==0:
    print(0)
elif lst.index(Min)!=len(lst)-1:
    while lst.index(Min)!=len(lst)-1:
        indexmin=lst.index(Min)
        indexelement=lst.index(Min)+1
        element=lst[indexelement]
        lst[indexelement],lst[indexmin]=Min,element
        t+=1
    while lst.index(max(lst))!=0:
        indexmax=lst.index(Max)
        indexelement2=lst.index(Max)-1
        element2=lst[indexelement2]
        lst[indexelement2],lst[indexmax]=Max,element2
        t+=1
    print(t)
        
