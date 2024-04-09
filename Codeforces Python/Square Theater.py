import math
x = str(input())
z = x.split(' ')
f = int(z[0]) / int(z[2])
f = math.ceil(f)
g = int(z[1]) / int(z[2])
g = math.ceil(g)
ans = f * g
print(ans)