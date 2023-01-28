#T is the number of test cases.
T = int(input())
#N is the number of pages
#M is the number of words on a page

l = [] #initializing a list to store output

for i in range(T):
    #N, M = int(input().split())
    #dont do this int(then input is wrong)
    N, M = map(int, input().split()) #run code is python3 otherwise python2 will show EOF for split method
    #print(N)
    #print(M)
    #print(N*M)
    l.append(N*M)

for each in l:
    print(each)
    



'''
T = int(input())

for i in range(T):
    a = input()
    z = a.split(" ")
    print(z)
    #n = int(x[0])
    #m = int(x[1])

    #print(n*m)

'''

'''
a = input()
print(a)

print(a.split())
'''