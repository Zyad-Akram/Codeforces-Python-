x=input().lower()
y= [i for i in x if i!='o' and i!='a'and i!='e' and i!='i'and i!='u'and i!='y']
print(y)
z=''
for i in y:
    z+='.'+i
print(z)
