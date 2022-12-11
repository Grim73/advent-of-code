f = open("input.txt", "r")
lines = f.readlines()
## one line function adding each occurence of `lines` to the list `calories`
games = [entry.strip() for entry in lines]

p1rock = "A"
p1paper = "B"
p1scissors = "C"

p2rock = "X"
p2paper = "Y"
p2scissors = "Z"

## Win states
rwin = "C X"
swin = "B Z"
pwin = "A Y"
pwcount = 0
swcount = 0
rwcount = 0


## Lose states
rloss = "B X"
sloss = "A Z"
ploss = "C Y"
plcount = 0
slcount = 0
rlcount = 0

draw = 0
draw_list = []
print(len(games))

for entry in games:
    if pwin == entry:
        pwcount += 2 + 6

    elif swin == entry:
        swcount += 3 + 6

    elif rwin == entry:
        rwcount += 1 + 6

    elif ploss == entry:
        plcount += 2

    elif sloss == entry:
        slcount += 3

    elif rloss == entry:
        rlcount +=1

    else:
        draw += 3
        draw_list.append(entry)

for strip in draw_list:
    ending = strip[-1]
    if ending == p2paper:
        draw += 2
    elif ending == p2scissors:
        draw += 3
    elif ending == p2rock:
        draw += 1

print(len(games))
wins = pwcount + swcount + rwcount
losses = plcount + slcount + rlcount

print(pwcount)
print(swcount)
print(rwcount)
print(plcount)
print(slcount)
print(rlcount)
print(draw)
print(wins + losses + draw)
