t = int(input())
 


result = []
for i in range(t):
    l = []
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
    # print(f'Round-Robin Matches between : {lFinal}')

    # print(reverse("12"))

    lInt = []
    for each in lFinal:
        lInt.append(int(each))

    x = []
    for each in lInt:
        x.append(each//10)

    xChota = set(x)
    xBada = list(xChota)

    # print(xChota)
    # print(xBada)

    d = {}
    for each in xBada:
        d[each] = 0
    # print(d)

    for each in lInt:
        # print(each)
        for every in xBada:
            # print(every)
            if((each//10)==every):
                d[every] = d[every] + 1
                # print('fuck')
            # print(d[every])
    print(d)

    restMatches = 0
    restTeams = n-2

    for each in d:
        if(each!=1):
            restMatches += d[each]

    print(restMatches)

    print(restTeams)
    print('yes')
    if(restTeams!=0):
        final =(restMatches//restTeams)
    else:
        final = 0

    result.append( (d[1]*3)-(final*3) )


for i in range(t):
    print(result[i])