x=int(input())
for i in range(x):
    out=0
    lst=input()
    lst=lst.split(' ')
    m=int(lst[0])
    n=int(lst[1])
    while m%n!=0:
        m+=1
        out+=1
    print(out)
    
