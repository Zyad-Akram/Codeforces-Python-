x=input()
x=x.split(' ')
y=input(' ')
y=y.split(' ')
z=int(x[1])
width=0
for i in y:
    if int(i)>z:
        width+=2
    else: width+=1
print(width)