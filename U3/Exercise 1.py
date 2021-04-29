import os


def loadFile(fileName):
    return open(fileName).read()


def getFileOfDirectory(dirPath):
    result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
    return result


def countDollar(string):
    return string.count("$")


print(countDollar(loadFile(r"spam\10.txt")))

print(loadFile(r"spam\10.txt"))

# file = open("emails.csv", "r")
#
# def countSpecialCharacters(file,character):
#     for line in file:
#         for char in line:
#
#
#
#
# count = 0
#
# for line in file:
#     line.lower()
#     for char in line:
#         if char == "h":
#             count += 1
# print(count)
