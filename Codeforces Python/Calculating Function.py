x=int(input())
Sum=0
if x%2==0:
    Sum=1*(x//2)
    print(Sum)
elif x%2!=0:
    Sum=((x//2)*1)-x
    print(Sum)