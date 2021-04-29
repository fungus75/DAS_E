import os


def loadFile(fileName):
    return open(fileName).read().lower()


def getFileOfDirectory(dirPath):
    result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
    return result


def countDollar(string):
    return string.count("$")


def amountWords(string):
    word_list = string.split()
    number_of_words = len(word_list)
    return number_of_words


def countStrangeWords(string):
    count = 0
    strange_word_list = ["porn", ".....", " , ", "penis", "viagra", "medicin", "rolex", "http ", " @ ", "money", "free",
                         "price", "sperm"]
    for word in strange_word_list:
        count += string.count(word)
    return count


def printOverview(string):
    print(string)
    print(amountWords(string))
    print(countDollar(string))


def wordstatistik(dir):
    dictionary = {}
    fileList = getFileOfDirectory(dir)
    for file in fileList:
        string = loadFile(f"{dir}/{file}")
        countWords(string, dictionary)
    return sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

def countWords(string, dictionary = {}):
    words = string.split()
    for word in words:
        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


print(wordstatistik("ham"))

#print(loadFile(r"spam\10.txt"))

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
