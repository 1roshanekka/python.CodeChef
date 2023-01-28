t = int(input())
l = []
for i in range(t):
    n = input()
    d = {}
    d["A"] = 0
    d["B"] = 0
    count = 0
    flag = 0
    for each in n:
        d[each] += 1
        count += 1
        if((count%2==0) and (d["A"]!=d["B"])):
            flag = 1
            break
        else:
            flag = 0
    if(flag==1):
        l.append('no')
    else:
        l.append('yes')
for i in range(t):
    print(l[i])


