t = int(input())

l = []
for i in range(t):
    x1,x2,x3,v1,v2 = map(int,input().split())
    #chef and kefa
    chefDist = abs(x1-x3)
    kefaDist = abs(x2-x3)
    if((chefDist/v1)>(kefaDist/v2)):
        l.append('Chef')
    elif((chefDist/v1)<(kefaDist/v2)):
        l.append('Kefa')
    else:
        l.append('Draw')

for i in range(t):
    print(l[i])

