x=list(input()) 
z=[]
for i in x:
    y=i
    if y not in z:
        z.append(i)
if len(z)%2!=0:
    print('IGNORE HIM!')
elif len(z)%2==0:
    print('CHAT WITH HER!')