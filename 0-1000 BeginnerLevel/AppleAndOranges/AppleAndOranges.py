# cook your dish here

x = int(input())
l = []
for i in range(x):
    n, m = map(int, input().split())
    # if(n%2==0 and m%2==0):
    #     if(max(n,m)%min(n,m)==0):
    #         l.append(min(n,m))
    #     else:
    #         l.append(min(n,m)//2)
    # elif( (n%2==0 and m%2!=0) or (n%2!=0 and m%2==0) ):
    #     l.append(1)
    if(max(n,m)%min(n,m)==0):
        l.append(min(n,m))
    else:
        l.append(min(n,m)//2)



for i in range(x):
    print(l[i])   