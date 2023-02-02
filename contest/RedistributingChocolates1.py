# cook your dish here
t = int(input())
l = []
for i in range(t):
    x, y, z =map(int,input().split())
    sum = x+y+z
    div = sum%3

    if((div==0)and(sum>3)):
        l.append('YES')
    else:
        l.append('NO')
    
    
for i in range(t):
    print(l[i])
# print(l)  