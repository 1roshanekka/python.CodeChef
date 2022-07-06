from typing import Final


# n = int(input())
# for i in range(n):
#     p, m, v = map(int, input().split())
#     FinalDecrease = p
#     if(p>1):
#         FinalDecrease = m-(p-1)
#         print(v*FinalDecrease)
#     else:
#         print(m*v)

# one time input and one time output

n = int(input())
l = []
for i in range(n):
    x = input()
    l.append(x)
for each in l:
    l1 = []
    l1 = each.split(' ')
    p = int(l1[0]) ; m = int(l1[1]) ; v = int(l1[2])
    FinalDecrease = p
    if(p>1):
        FinalDecrease = m-(p-1)
        print(v*FinalDecrease)
    else:
        print(m*v)