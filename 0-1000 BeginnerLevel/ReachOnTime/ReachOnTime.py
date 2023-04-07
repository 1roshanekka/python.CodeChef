n = int(input())
l = []
for i in range(n):
    leaveTime = int(input())
    if(leaveTime>=30):
        l.append('YES')
    else:
        l.append('NO')
for i in range(n):
    print(l[i])

                    
