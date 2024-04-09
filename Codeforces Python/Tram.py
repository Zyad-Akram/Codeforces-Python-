x=int(input())
Min=0
reminder=0
z=[]
for i in range(x):
    y=input()
    y=y.split(' ')
    z.append(y)
for i in range(len(z)):
    for ii in range(len(z[i])-1):
        ex=int(z[i][ii])
        en=int(z[i][ii+1])
        reminder=(-ex+en)+reminder
        if reminder>Min:
            Min=reminder
print(Min)
