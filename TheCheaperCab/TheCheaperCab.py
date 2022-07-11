from sys import api_version

from numpy import append


T = int(input())
l = []
for each in range(T):
    X, Y = map(int, input().split())
    if(X>Y):{
        l.append("SECOND")
    }
    elif(Y>X):{
        l.append("FIRST")
    }
    elif(X==Y):{
        l.append("ANY")
    }

for each in l:
    print(each)
