x=input()
x=x.split(' ')
y=int(x[1])
z=int(x[0])
while y!=0:
    if z%10==0:
        z=z/10
    elif z%10!=0:
        z-=1
    y-=1
print(int(z))
