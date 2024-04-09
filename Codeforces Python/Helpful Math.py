x=input()
y=x.split('+')
y.sort()
m=''
for i in y:
    m=m+i+'+'
m=m[:len(m)-1]
print(m)