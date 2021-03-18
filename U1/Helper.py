def vigenereCoder(text, key, encode=True):
    key=key.lower()
    keyNumbers=[]
    for keyChar in key:
        ascii=ord(keyChar)
        if ascii < 97 or ascii > 122:
            continue
        keyNumbers.append(ascii-97)

    keyPos=0
    keyLen=len(keyNumbers)
    result=""
    for char in text:
        ascii = ord(char.lower())
        if ascii < 97 or ascii > 122:
            result+=char
            continue

        charCode=ascii-97
        if encode:
            newCharCode=charCode+keyNumbers[keyPos]
        else:
            newCharCode=charCode-keyNumbers[keyPos]

        newCharCode=newCharCode%26

        if ord(char)>=97:
            result+=chr(97+newCharCode)
        else:
            result+=chr(65+newCharCode)

        keyPos+=1
        if keyPos>=keyLen:
            keyPos=0

    return result


def vigenere_encrypt(text,key):
    return vigenereCoder(text,key,True)

def vigenere_decrypt(cipertext,key):
    return vigenereCoder(cipertext,key,False)

def vigenere_getKey(text,cipertext):
    if len(text) != len(cipertext):
        return None

    key=""
    for i in range(0,len(text)):
        ordText=ord(text[i])
        ordCiper=ord(cipertext[i])

        if ordText>97:
            ordText-=97

        if (ordCiper>97):
            ordCiper-=97

        if ordText>65:
            ordText-=65

        if (ordCiper>65):
            ordCiper-=65

        ordKey=(ordCiper-ordText)%26
        key+=chr(97+ordKey)

    return key

def getRelevantElementsInfile(filename):
    file=open(filename,"r")
    fullFile=file.read()
    fullFile=fullFile.lower()
    # remove all non-alphabetic chars
    fullWorkfile=''.join([i for i in fullFile if i.isalnum()])
    return fullWorkfile

def findPairsInFile(filename,pairSize,minFound=2,maxCheckSize=1000):
    fullWorkfile=getRelevantElementsInfile(filename)
    checkFirstChars=min(maxCheckSize,len(fullWorkfile)-pairSize)
    results=[]
    foundParts=[]
    for checkPos in range(0,checkFirstChars):
        checkPart=fullWorkfile[checkPos:checkPos+pairSize]
        if checkPart in foundParts:
            continue
        foundParts.append(checkPart)
        foundAmount=1
        foundDeltas=[]
        startPos=checkPos
        try:
            while (fullWorkfile.index(checkPart,startPos+1))>=0:
                newPos=fullWorkfile.index(checkPart,startPos+1)
                delta=newPos-startPos
                startPos=newPos
                foundDeltas.append(delta)
                foundAmount+=1
        except:
            pass
        if foundAmount>=minFound:
            foundDeltas.sort()
            results.append({'Part':checkPart,'Count':foundAmount,'Deltas':foundDeltas})
    results.sort(key=lambda item: item.get("Count"), reverse=True)
    return results

def printArray(array):
    for element in array:
        print(element)

def getCharStats(filename):
    chrCounter = []
    for i in range(ord('a'), ord('z') + 1):
        chrCounter.append({"letter": chr(i), "Count": 0})

    file = open(filename, "r")
    # read file per line
    for line in file:
        line = line.lower()
        for char in line:
            ordValue = ord(char)
            if (ordValue <= 122 and ordValue >= 97):
                alphabetNumber = ordValue - 97
                updatedValue = chrCounter[alphabetNumber].get('Count') + 1
                chrCounter[alphabetNumber].update({'Count': updatedValue})
    chrCounter.sort(key=lambda item: item.get("Count"), reverse=True)
    return chrCounter

def getCharIndexInStats(relevantPart, charStat):
    result=[]
    relevantPart=relevantPart.lower()
    for char in relevantPart:
        index=0
        for statLine in charStat:
            if statLine.get("letter") == char:
                result.append({"letter":char,"position":index})
            index+=1
    return result



def encodeSubst(text,alphabet):
    result=""
    text=text.lower()
    for char in text:
        ascii=ord(char)
        if ascii <97 or ascii > 122:
            result+=char
            continue

        ascii=ascii-97
        newchar=alphabet[ascii]
        result+=newchar
    return result

def generateSubstDecodeAlphabet(alphabet):
    result=[" "]*26
    alphabet=alphabet.lower()
    for i in range(0,26):
        c=alphabet[i]
        n=ord(c)-97
        result[n]=chr(97+i)
    return ''.join(result)



def decodeSubst(text,alphabet):
    alphabet=generateSubstDecodeAlphabet(alphabet)
    return encodeSubst(text,alphabet)