# cook your dish here

t = int(input())

l1=[]

for i in range(t):
    l = []
    n = int(input()) #length of string s
    s = input()
    count = 0
    # for each in s:
    #     l.append(each)

    for i in range(len(s)):
        if(s[i] in l):
            # print('yes')
            count=1
            break
        else:
            l.append(s[i])

    if(count==1):
        d = {}
        for each in s:
            d[each] = 0
        
        for each in s:
            d[each] = d[each] + 1
        
        Key_max = max(d, key = d.get)  
        l1.append(len(s)-d[Key_max])
        # print(d)
        # print(Key_max)

    else:
        l1.append(-1)
        
for i in range(t):
    print(l1[i])