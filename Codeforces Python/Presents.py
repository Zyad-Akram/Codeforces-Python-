x=int(input())
y=input()
y=y.split(' ')
lst=[]
c=0
i=0
out=''
for ii in y:
    lst.append(int(ii))
while c!=x:
    i+=1
    m=lst.index(i)
    m+=1
    m=str(m)
    out+=m+' '
    c+=1
print(out)