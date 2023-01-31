t = int(input())
 
l = []
x = ()
for i in range(t):
    n = int(input())
    count = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i!=j):
                l.append(str(i)+str(j))

def reverse(x):
    a = str(x)
    z = ""
    for i in range(len(a)-1, -1,-1):
        z = z+ a[i]
    return z

lFinal = []           
for each in l:
    # print(each)
    if( (reverse(each) in lFinal) == False):
        lFinal.append(each)
    # print(reverse(each) in l)
    # print(reverse(each))
    # print('--')
#print(f'Combinations are : {l}')
print(f'Round-Robin Matches between : {lFinal}')

# print(reverse("12"))

