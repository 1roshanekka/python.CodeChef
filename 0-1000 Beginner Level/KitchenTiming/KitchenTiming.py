t = int(input())
l =[]
for i in range(t):
    x, y = map(int, input().split())
    l.append(abs(x-y))

for i in range(t):
    print(l[i])