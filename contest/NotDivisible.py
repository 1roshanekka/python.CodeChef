# cook your dish here
t = int(input())
l = []
result = [] 
for k in range(t):
    n = int(input())
    #n is the length of array

    #j-i+1
    #combinations of pair
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
    # print(f'Round-Robin Matches between : {lFinal}')
    lFinalInt = []
    for each in lFinal:
        lFinalInt.append(int(each))

    a = max(lFinalInt)
    b = min(lFinalInt)
    # print(a,b)
    chota = b//10
    bada = a%10
    # print(lFinalInt)
    tot = len(lFinal)
    divisor = bada-chota+1
    # print(bada,chota)
    print(divisor)
    

    those = []
    for i in range(1000):
        if(i%divisor!=0):
            those.append(i)
    
    #those[] contains number which are not divisble

    #now split in 3
    def calc(x,y):
        if()

# for i in range(t):
#     print(result[i])