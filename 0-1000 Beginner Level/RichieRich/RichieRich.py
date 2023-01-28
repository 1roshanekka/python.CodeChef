# cook your dish here
#chef has A billion dollars and he aims to increase assets by X billion dollars per year
#how many years will it take to grow considering than none other are competing
#to be richest he needs to have worth B billions dollars atleast

n = int(input())

l = []

for i in range(n):
    a,b,x = map(int,input().split())
    increase = b-a
    time = increase//x
    l.append(time)

for i in range(n):
    print(l[i])
    