x=input()
y=input()
if ord(x[0])>ord(y[0]):
    print(-1)
elif ord(x[0])<ord(y[0]):
    print(1)
elif ord(x[0])==ord(y[0]):
    print(0)