x=int(input())
z=input()
y=[]
for i in range(len(z)-1):
    if z[i]==z[i+1]:
        y.append(z[i])
print(len(y))