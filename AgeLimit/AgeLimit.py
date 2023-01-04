#minimum age limit is x 
#age should be grater than or equal to x

#max age should be y

n = int(input())
d = {}


l = []

for i in range(n):
    x,y,a = map(int, input().split())
    if(x<=a<y):
        l.append('YES')
    else:
        l.append('NO')

for i in range(n):
    print(l[i])

