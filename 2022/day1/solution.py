f = open("input.txt", "r")
lines = f.readlines()
## one line function adding each occurence of `lines` to the list `calories`
calories = [entry.strip() for entry in lines]

## Creates an empty list for your calories to be input
elf_sums = []
current_sum = 0

## Setting up the loop to add each line
for entry in calories:
    if entry != '':
        current_sum += int(entry)
    ## If the line is blank, append the current_sum to the list,
    ### resetting the loop
    elif entry == '':
        elf_sums.append(current_sum)
        current_sum = 0
elf_sums.append(current_sum)

print(max(elf_sums))

## Part 2

top_total = []
count = 0



while count <=2:
    ## 
    top_total.append(max(elf_sums))

    elf_sums.remove(max(elf_sums))
    count += 1

total = 0

for grand_total in top_total:
    total += grand_total

print(total)
