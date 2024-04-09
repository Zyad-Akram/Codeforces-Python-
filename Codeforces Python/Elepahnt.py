x=int(input())
y=0
while x!=0:
    if x>=5:
        x-=5
    elif x==4:
        x-=4
    elif x==3:
        x-=3
    elif x==2:
        x-=2
    elif x==1:
        x-=1
    y+=1
print(y)