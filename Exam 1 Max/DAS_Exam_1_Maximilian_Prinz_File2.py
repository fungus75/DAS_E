# DAS E Exam 15.04.2021
# Variables:
count = 0
# Open file
file = open("RandomText.txt", "r")
# read file per line
for line in file:
    #lower to catch all
    line.lower()
    for char in line:
        if char == "p":
            count += 1

print(count)



