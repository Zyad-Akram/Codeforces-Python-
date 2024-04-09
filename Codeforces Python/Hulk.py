x=int(input())
out='I hate'
if x==1:
    print(out+' it')
else:
    for i in range(1,x):
        if (i+1)%2==0:
            out+=' that I love'
        elif (i+1)%2!=0:
            out+=' that I hate'
    print(out+' it')