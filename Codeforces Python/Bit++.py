x=int(input())
Acc=0
for i in range(x):
    y=input()
    for i in y:
        if i=='+':
            Acc+=1
            break
        elif i=='-':
            Acc-=1
            break
print(Acc)