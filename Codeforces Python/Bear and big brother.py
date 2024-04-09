x=input()
x=x.split(' ')
a=int(x[0])
b=int(x[1])
y=0
while a<=b:
    y+=1
    a=a*3
    b=b*2
print(y)