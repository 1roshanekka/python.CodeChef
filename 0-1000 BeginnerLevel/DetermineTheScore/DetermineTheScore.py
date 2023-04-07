# cook your dish here
n = int(input())

l = []
for i in range(n):
    score, test = map(int, input().split())
    if(test==0):
        l.append(0)
    else:
        l.append((score//10)*test)
for i in range(n):
    print(l[i])