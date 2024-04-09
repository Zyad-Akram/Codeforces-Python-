x='hello'
s=str(input())
def chat():
    y=0
    for i in s:
        if i==x[y]:
            y=y+1
            if y==5:
                return'YES'
    return 'NO'
print(chat())
        