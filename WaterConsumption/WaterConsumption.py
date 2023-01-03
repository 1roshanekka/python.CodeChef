#drink at least 2000ml each day
x = int(input())
l = []
for i in range(x):
    n = int(input())
    l.append(n)


for i in range(x):
    if(l[i]>=2000):
        print('YES')
    else:
        print('NO')

