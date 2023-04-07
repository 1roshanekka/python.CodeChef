# cook your dish here
#taken dose in D days earlier

#will take the doze no less than L days and no more than R days 

n = int(input())

ls =[]

for i in range(n):
    d,l,r = map(int, input().split())
    if(l<=d<=r):
        ls.append('Take second dose now')
    elif(d<r):
        ls.append('Too Early')
    elif(d>l):
        ls.append('Too Late')
        
for i in range(n):
    print(ls[i])