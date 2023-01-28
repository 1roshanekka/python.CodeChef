t = int(input())
l = []
for i in range(t):
    n , k = map(int, input().split())
    #n kids and k weapons
    l.append(k//n)
for i in range(t):
    print(l[i])


