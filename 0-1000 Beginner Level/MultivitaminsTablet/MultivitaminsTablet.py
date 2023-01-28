n = int(input())


l = []
for i in range(n):
    x,y = map(int,input().split())
    #take tablets 3 times a day for next X days
    #he has Y tablets
    #find if he has enough tablets for these x days

    if(y>=(x*3)):
        l.append('YES')
    else:
        l.append('NO')

for i in range(n):
    print(l[i])

