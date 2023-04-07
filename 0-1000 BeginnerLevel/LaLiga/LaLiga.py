n = int(input())
l = []
for i in range(n):
    d = {}
    for i in range(4):
        x,y =  map(str, input().split())
        d[x] = int(y)
    # print(d)
    # print(d["RealMadrid"])
    # if(d["RealMadrid"]==d["Malaga"]):
    #     #draw
    #     #As RealMadrid has more score than Barcelona it wins
    #     l.append("RealMadrid")
    if(d["RealMadrid"]<d["Malaga"]) and (d["Barcelona"]>d["Eibar"]):
        l.append("Barcelona")
    else:
        l.append("RealMadrid")

for i in range(n):
    print(l[i])
