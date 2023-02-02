# cook your dish here
t = int(input())
l = []
for i in range(t):
    x, y, z =map(int,input().split())
    sum = x+y+z
    count = 1
    a,b,c = 0

    while(count<=sum):
        if(count+3==0):
            a += 1
        elif(count%2==0):
            b += 1
        elif(count%3==0)
            c += 1        

    # l.append(min(x,y,z))
    fast = min(x,y,z)
    if(x==fast):
        l.append('Alice')
    elif(y==fast):
        l.append('Bob')
    elif(z==fast):
        l.append('Charlie')

    
for i in range(t):
    print(l[i])
# print(l)  