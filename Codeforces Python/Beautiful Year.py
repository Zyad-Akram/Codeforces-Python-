x=int(input())
lst=[]
x+=1
x=str(x)
while x[0]==x[1] or x[0]==x[2] or x[0]==x[3] or  x[1]==x[2] or x[1]==x[3] or x[2]==x[3]:
    x=int(x)+1
    x=str(x)
print(x)
