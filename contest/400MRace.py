# cook your dish here
t = int(input())
l = []
for i in range(t):
    x, y, z =map(int,input().split())
    distance = 400
    AliceSpeed = distance/x
    BobSpeed = distance/y
    CharlieSpeed = distance/z

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