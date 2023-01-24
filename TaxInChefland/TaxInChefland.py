# cook your dish here
l = []
n = int(input())
for i in range(n):
    income = int(input())
    if(income>100):
        l.append(income-10)
    else:
        l.append(income)
        
for i in range(n):
    print(l[i])