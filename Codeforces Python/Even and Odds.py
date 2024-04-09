x=input()
x=x.split(' ')
number=int(x[0])
position=int(x[1])
if number%2!=0:
    if position<=number/2:
        print((2*position)-1)
    else: print((2*position)-(number+1))
elif number%2==0:
    if position>number/2:
        y=number/2
        print(int(((-y+position)*2)))
    elif position<=number/2:
        i=0
        m=number/2
        while i!=position:
            k=0
            k=(number/2)-(m)
            m-=1
            i+=1
        print(int(k+position))