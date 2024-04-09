x=input()
x=x.split(' ')
y=[int(x[0]),int(x[2])]
z=0
for i in range(y[1]):
    z+=y[0]*(i+1)
m=int(x[1])-z
if m<0:
    print(-m)
else: print(0)