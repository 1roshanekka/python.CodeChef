z = int(input())
l = []
for i in range(z):        
    n = int(input())
    l.append(n)

for i in range(z):
    if(0<l[i]<4):
        print('MILD')
    elif(4<=l[i]<7):
        print('MEDIUM')
    elif(l[i]>=7):
        print('HOT')