x=int(input())
y=input()
y=y.split(' ')
y.pop(0)
z=input()
z=z.split(' ')
z.pop(0)
Sum=0
for i in range(x):
    m=str(i+1)
    if m in y or m in z:
        Sum+=1
if Sum==x:
    print('I become the guy.')
else: print('Oh, my keyboard!')