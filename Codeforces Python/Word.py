x=str(input())
C=0
s=0
for i in x:
    if ord(i)<=90:
        C+=1
    else:
        s+=1
if C>s:
    print(x.upper())
else:
    print(x.lower())    