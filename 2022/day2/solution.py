f = open("input.txt", "r")
lines = f.readlines()
## one line function adding each occurence of `lines` to the list `calories`
games = [entry.strip() for entry in lines]
print(games)

p1rock = "A"
p1paper = "B"
p1scissors = "C"

p2rock = "Y"
p2paper = "X"
p2scissors = "Z"

#pwin = ["A" , "X" ]
#swin = ["B" , "Z"]
#rwin = ["C" , "Y"]
#pcount = 0
#scount = 0
#rcount = 0
#loses = 0

#for entry in games:
#    if pwin == entry:
#        pcount += 1
#    elif swin == entry:
#        scount +=1
#    elif rwin == entry:
#        rcount +=1
#    else:
#        loses += 1
#
#
#print(pcount)
#print(scount)
#print(rcount)
#print(loses)


