lst=[]
for i in range(3):
    lst.append(int(input()))
Maxi1=sum(lst)
Maxi2=lst[0]*lst[1]*lst[2]
Maxi3=(lst[0]+lst[1])*lst[2]
Maxi4=lst[0]*(lst[1]+lst[2])
Maxi5=lst[0]+lst[1]*lst[2]
Maxi6=lst[0]*lst[1]+lst[2]
lst2=[Maxi1,Maxi2,Maxi3,Maxi4,Maxi5,Maxi6]
print(max(lst2))