x=input()
y=1
for i in range(len(x)-1):
    if x[i]==x[i+1]:
        y+=1
    elif x[i]!=x[i+1]:
        y=1
    if y==7:
        print('YES')
        break
if y<7:
    print('NO')
