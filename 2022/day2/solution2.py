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


def set_state(state_list, dest_list, points):
    score = 0
    for entry in games:

        if entry == state_list[0]:
            dest_list[0].append(entry)
            score += points

        elif entry == state_list[1]:
            dest_list[1].append(entry)
            score += points

        else:
            dest_list[2].append(entry)
            score += points

set_state(win, rock, 3)
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
print(len(rock[0]))
print(len(paper[0]))
print(len(scissors))
print(score)
