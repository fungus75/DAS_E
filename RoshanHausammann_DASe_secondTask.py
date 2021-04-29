file = open("exam.txt", "r")

count = 0

for line in file:
    line.lower()
    for char in line:
        if char == "h":
            count += 1
print(count)
