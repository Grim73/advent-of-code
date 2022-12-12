f = open("input.txt", "r")
lines = f.readlines()
## one line function adding each occurence of `lines` to the list `calories`
games = [entry.strip() for entry in lines]

win = ["C X", "A Y", "B Z"]
loss = ["B X", "C Y",  "A Z"]
shape = ["X", "Y", "C"]
rock = [[],[],[]]
paper = [[],[],[]]
scissors = [[],[],[]]
draw = []

score = []


def set_state(state1, state2, dest1, dest2, dest3, dest4):

    for entry in games:

        if entry == state1[0]:
            dest1[0].append(entry)


        elif entry == state1[1]:
            dest2[0].append(entry)

        elif entry == state1[2]:
            dest3[0].append(entry)

        if entry == state2[0]:
            dest1[1].append(entry)

        elif entry == state2[1]:
            dest2[1].append(entry)

        elif entry == state2[2]:
            dest3[1].append(entry)
        else:
            dest4.append(entry)

    for strip in dest4:
        ending = strip[-1]

        if ending == "X":
            dest1[2].append(ending)

        elif ending == "Y":
            dest2[2].append(ending)

        else:
            dest3[2].append(ending)


set_state(win, loss, rock, paper, scissors, draw)

##for entry in games:
##
##    if entry == win[0]:
##        rock[0].append(entry)
##        score +=1
##
##    elif entry == win[1]:
##        paper[0].append(entry)
##        score += 2
##
##    elif entry == win[2]:
##        scissors[0].append(entry)
##        score += 3
##
##    elif entry == loss[0]:
##        rock[1].append(entry)
##        score +=1
##
##    elif entry == loss[1]:
##        paper[1].append(entry)
##        score += 2
##
##    elif entry == loss[2]:
##        scissors[1].append(entry)
##        score += 3
##    else:
##        ending = entry[-1]
##        draw.append(ending)
##        if ending == shape[0]:
##            rock[2].append(ending)
##            score +=1
##        elif ending == shape[1]:
##            paper[2].append(ending)
##            score += 2
##        else:
##            scissors[2].append(ending)
##            score += 3
##
## def scoring(throw, points):

##["B X", "C Y",  "A Z"]
print(len(rock[2]))
print(len(paper[0]))
print(len(scissors))
print(score)
