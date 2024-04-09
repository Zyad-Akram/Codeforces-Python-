x=str(input())
m=x.split(' ')
lst=[]
z=0
y=str(input())
y=y.split(' ')
y=list(map(int, y))
max=y[int(m[1])-1]
if max==0:
    for i in y:
        if i==0:
            lst.append(i)
    print(len(y)-len(lst))
else:
    for i in y:
        if i>=max:
            z=z+1
    print(z)
