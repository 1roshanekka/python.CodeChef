
#T is the number of test cases
T = int(input())
l = [] #list to store the results

for each in range(T):
    X, Y = map(int, input().split())
    if(X>Y):{ #between cab X & Y ,if cab X is costing more than cab Y then second one is cheaper
        l.append("SECOND")
    }
    elif(Y>X):{#between cab X & Y ,if cab Y is costing more than cab X then first one is cheaper
        l.append("FIRST")
    }
    elif(X==Y):{#between cab X & Y , both cost the same so any one can be used to ride
        l.append("ANY")
    }

for each in l:
    print(each) #printing results of each test cases
