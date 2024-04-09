x=int(input())
y=input()
y=y.split(' ')
lst=[]
for i in y:
    lst.append(int(i))
print(float(sum(lst)/x))