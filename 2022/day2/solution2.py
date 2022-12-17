f = open("input.txt", "r")
lines = f.readlines()
## one line function adding each occurence of `lines` to the list `calories`
games = [entry.strip() for entry in lines]

win = ["C X", "A Y", "B Z"]
loss = ["B X", "C Y",  "A Z"]
shape = ["X", "Y", "C"]
states = [[], [], []]
winner = []
lose = []
draw = []

score_bank = [[], [], []]
score = 0

extraction = []

## This function runs the input list and sorts it into its defined state
## 
def set_state(state1, state2, dest1, dest2, dest3):

    for entry in games:

        if entry == state1[0]:
            dest1.append(entry)

        elif entry == state1[1]:
            dest1.append(entry)

        elif entry == state1[2]:
            dest1.append(entry)

        if entry == state2[0]:
            dest2.append(entry)

        elif entry == state2[1]:
            dest2.append(entry)

        elif entry == state2[2]:
            dest2.append(entry)
        else:
            dest3.append(entry)


## Set score of each win/loss/draw based on shape score
## def set_score (state1, state2, state3, shape, points):





##    for strip in state3:
##        ending = strip[-1]
##
##        if ending == "X":
##            dest1.append(ending)
##
##        elif ending == "Y":
##            dest2.append(ending)
##
##        else:
##            dest3.append(ending)
##
## Step 2 - X == draw, Y == Win, Z == Loss



set_state(win, loss, winner, lose, draw)

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
print(len(winner))
print(len(lose))
print(len(draw))
print(score)
print(states)
