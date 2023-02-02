t = int(input())
l = []
for i in range(t):
    n, x, y = map(int,input().split())
    if(n<=(x*y)):
        l.append('YES')
    else:
        l.append('NO')

for i in range(t):
    print(l[i])