#chef has A patties and B buns 
#to make a burger he need 1 patty and 1 bun
#find the max numbers of burgers he can make

n = int(input())

l = []

for i in range(n):
    a,b = map(int, input().split())
    l.append(min(a,b))

for i in range(n):
    print(l[i])


