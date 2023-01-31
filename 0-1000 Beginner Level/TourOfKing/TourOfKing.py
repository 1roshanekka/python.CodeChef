t = int(input())
l = []
for i in range(t):
    n,m = map(int, input().split())
    #n is 5 seater 
    #m is 7 seater 
    l.append((n*5)+(m*7))
for i in range(t):
    print(l[i])