n = int(input())

l = []
for i in range(n):
    x = int(input())
    if(x==6):
        l.append('YES')
    else:
        l.append('NO')

for i in range(n):
    print(l[i])