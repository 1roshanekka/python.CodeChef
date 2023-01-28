#each set contains 15 squats
n = int(input()) #number of inputs

l = []
for i in range(n):
    x = int(input())
    l.append(x)

for i in range(n):
    print(l[i]*15)
