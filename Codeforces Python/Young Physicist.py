f=int(input())
lst=[]
lst1=[]
Sum=0
for i in range(f):
    User=input()
    lst.append(User.split(' '))
for ii in range(f):
    for i in range(f):
        Sum+=int(lst[i][ii])
    if Sum!=0:
        print('NO')
    break
if Sum==0:
    print('YES')
