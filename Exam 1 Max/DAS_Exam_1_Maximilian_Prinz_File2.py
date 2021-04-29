# DAS E Exam 15.04.2021
# Function

def counter(file, letter):
    count = 0
    for line in file:
        #lower to catch all
        line.lower()
        for char in line:
            if char == letter:
                count += 1
    return count


# Open file
file = open("RandomText.txt", "r")
print(counter(file,"p"))



