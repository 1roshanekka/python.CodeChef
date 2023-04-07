t= int(input())
l = []
for i in range(t):
    x, y = map(int, input().split())
    if(x>y):
        l.append(x-y)
    else:
        l.append(0)

for i in range(t):
    print(l[i])