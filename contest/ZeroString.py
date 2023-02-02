# cook your dish here
t = int(input())
l = []

def dekho(x):
    zero = 0
    one = 0
    for each in x:
        if(each=='0'):
            zero += 1
        elif(each=='1'):
            one += 1
    return (zero)


    
for i in range(t):
    n = int(input())
    s = input()

    zeroes = dekho(s)
    ones = len(s)-zeroes

    # print(ones,zeroes)

    #already 0
    if(zeroes==len(s)):
        l.append(0)
    
    #if ones > zeroes
    elif(ones>zeroes):
        l.append(1+zeroes)
    
    #if zeroes > ones
    elif(zeroes>ones):
        l.append(ones)
    
    #if zeroes = ones
    elif(zeroes==ones):
        l.append(zeroes)
    

for i in range(t):
    print(l[i])