x=int(input())
y=0
z=0
for i in range(x):
    w=str(input())
    for i in w:
        if i=='1':
            y+=1
        else: pass
    if y==2 or y==3:
        z=z+1
    y=0
print(z)