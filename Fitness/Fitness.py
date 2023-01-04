#distance from office and house is x kms and goes to office 5 days a week
#find the number of kms he travelled in a week

n = int(input()) #number of test cases

l = []
for i in range(n):
    x = int(input())
    dist = x*2*5
    l.append(dist)

for i in range(n):
    print(l[i])