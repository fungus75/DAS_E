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


def countFlagWords(string):
    count = 0
    strange_word_list = ["....", "penis", "iagra", "medicin", "rolex", "http","money", "free",
                         "price", "sperm", "microsoft", "pills", "xxx","medizin", "orn",'|', 'font', "td", "nbsp", "www", "moagra", "adobe", "xp"]
    for word in strange_word_list:
        count += string.count(word)
    return count

def flagWords(string):
    pass

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
    return dictionary

def countWords(string, dictionary = {}):
    words = string.split()
    for word in words:
        if word in dictionary.keys():
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary


def CommonSpamWords():
    ham_dic = wordstatistik("ham")
    spam_dic = wordstatistik("spam")

    #spamÜberschuss = all(map( spamDic.pop, hamDic))
    res = {key: spam_dic[key] - ham_dic.get(key, 0)
                           for key in spam_dic.keys()}
    print(dict(sorted(res.items(), key=lambda item: item[1])))

def strangeWordsFaktor(string):
    count = countFlagWords(string)
    amount = amountWords(string)
    faktor = count/amount
    return faktor


def isspam(string):
    if countDollar(string) > 2 or string.count("#") > 4 or string.count("%") > 2 or string.count("?") > 6 or string.count("dollar") > 0 or string.count("!") > 2:
        return True
    if countFlagWords(string) > 1:
        return True
    if strangeWordsFaktor(string) > 0.02:
        return True
    if len(string)< 60:
        return True


def spamstatistik(dir):
    dictionary = {}
    fileList = getFileOfDirectory(dir)
    spamcount = 0
    for file in fileList:
        string = loadFile(f"{dir}/{file}")
        if isspam(string):
            spamcount += 1
    faktor = spamcount/len(fileList)
    return faktor

print(spamstatistik("ham"))
print(spamstatistik("spam"))

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
