x=int(input())
y=input()
y=y.split(' ')
i=0
Max=0
num=0
while i+1!=len(y):
    while y[i]>=y[i+1]:
        num+=1
        i+=1
    if num>Max:
            Max=num
            num=0
    i+=1
print(Max) 