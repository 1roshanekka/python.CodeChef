t = int(input())
l=[]
for i in range(t):
    x,y = map(int, input().split())
    if(x<y):
        l.append('Profit')
    elif(x>y):
        l.append('Loss')
    else:
        l.append('Neutral')

for i in range(t):
    print(l[i])
    