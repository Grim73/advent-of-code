f = open("input.txt", "r")
lines = f.readlines()
## one line function adding each occurence of `lines` to the list `calories`
games = [entry.strip() for entry in lines]

win = ["C X", "A Y", "B Z"]
loss = ["B X", "C Y",  "A Z"]
rock = []
paper = []
scissors = []
draw = []
for entry in games:
    
    if entry == win[0]:
        rock.append(entry)

    elif entry == win[1]:
        paper.append(entry)
    
    elif entry == win[2]:
        scissors.append(entry)

    elif entry == loss[0]:

    else:
        


##["B X", "C Y",  "A Z"]
print(len(rock))

