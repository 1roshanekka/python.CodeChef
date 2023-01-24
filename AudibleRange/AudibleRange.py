n = int(input())
l = []
for i in range(n):
    freq = int(input())
    if(67<=freq<=45000):
        l.append('YES')
    else:
        l.append('NO')
for i in range(n):
    print(l[i])
