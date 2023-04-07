t = int(input())
l = []
for i in range(t):
    x,y = map(int, input().split())
    l.append((10*x)+(y*90))

for i in range(t):
    print(l[i])