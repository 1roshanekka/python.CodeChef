n = int(input())

l = []
for i in range(n):
    x = input()
    flag = 0
    for each in x:
        if(each==str(7)):
            flag = 1
            break
        else:
            flag=0
    if(flag==1):
        l.append('YES')
    else:
        l.append('NO')

for i in range(n):
    print(l[i])


    