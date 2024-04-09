x=input()
x=x.split(' ')
m=int(x[1])
y=input()
z=[]
for i in y:
    z.append(i)
while m!=0:
    i=0
    while i<(len(z)-1):
        if z[i]=='B' and z[i+1]=='G':
           z[i],z[i+1]=z[i+1],z[i]
           i+=1
        i+=1  
    m-=1
f=''.join(z)
print(f)