# X weeks
# Y coins for a week

#First line of input is an integer T which denotes the number of test cases
#Afterwards the lines contain X and Y respectively

n = int(input())

#initialising the lists
X = []
Y = []

for i in range(n):
    x , y = map(int, input().split()) #we assume input as string and then split the input into two integers and map them
    X.append(x)
    Y.append(y)

#printing the output
for j in range(n):
    print(X[j]*Y[j]) #total coins required by the chef need to pay to learn from classes
