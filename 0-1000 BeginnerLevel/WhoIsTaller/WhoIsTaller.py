n = int(input())
l = []
for i in range(n):
    x,y = map(int,input().split())
    if(x>y):
        l.append('A')
    else:
        l.append('B')
for i in range(n):
    print(l[i])
    
