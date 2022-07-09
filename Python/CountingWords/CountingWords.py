#T is the number of test cases.
T = int(input())
#N is the number of pages
#M is the number of words on a page
for i in range(T):
    #N, M = int(input().split())
    #dont do this int(then input is wrong)
    N, M = map(int, input().split())
    print(N)
    print(M)
    #print(N*M)
