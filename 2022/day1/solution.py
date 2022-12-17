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
## Creating a list to hold the top three amounts
top_total = []
count = 0
total = 0



while count <=2:
    ## Append the largest amount in the first list into the new list
    ## then delete that element
    top_total.append(max(elf_sums))

    elf_sums.remove(max(elf_sums))
    count += 1

## Add all numberd in list to `total`
for grand_total in top_total:
    total += grand_total

print(total)
