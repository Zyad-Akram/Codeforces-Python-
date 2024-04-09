x=int(input())
out=0
for i in range(x):
    y=input()
    y=y.split(' ')
    if int(y[1])-int(y[0])>=2:
        out+=1
print(out)