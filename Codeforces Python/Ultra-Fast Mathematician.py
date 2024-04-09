x=input()
y=input()
ans=''
for i in range(len(x)):
    if x[i]!=y[i]:
        ans+='1'
    else: ans+='0'
print(ans)