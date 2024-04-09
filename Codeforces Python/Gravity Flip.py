x=int(input())
y=input()
y=y.split(' ')
lst=[]
for i in y:
    lst.append(int(i))
lst.sort()
out=''
for i in lst:
    m=str(i)
    out+=m+' '
print(out)