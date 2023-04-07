t = int(input())
l = []

for i in range(t):
    x,h = map(int,input().split())
    if(x>=h):
        l.append('YES')
    else:
        l.append('NO')
    
for i in range(t):
    print(l[i])
    
    