import math
#len of a is N
t = int(input())

def totta():

    n, y = map(int, input().split())
    a = (input().split())
    tot = int(0)
    for i in range(len(a)):
        tot = tot | int(a[i]) 
    
    # print(tot)  
    ans=-1
    l = 0
    r  = int(math.pow(2,20) + 10)
    # print(r)
    while(l<=r):
        mid =int((l+r)/2)
        if((tot | mid) == y):
            ans=mid
            r=mid-1
        elif((tot|mid)>y):
            r=mid-1 
        else:
            l=mid+1
    return(ans)
z = [] 
for i in range(t):
    z.append(totta())
for i in range(t):
    print(z[i])