from Helper1 import *

charStat=getCharStats("crypt2.txt")
print(charStat)

englishWeights="ETAOINSRHDLUCMFYWGPBVKXQJZ".lower()
alphabetHelp=[' ']*26
for i in range(0,26):
    clear=englishWeights[i]
    encoded=charStat[i].get("letter")
    alphabetHelp[ord(clear)-97]=encoded
alphabet=''.join(alphabetHelp)

print(alphabet)

# mbcgs = hours
# xmau  = than
# dnss  = less
# knzbegaxs = democrats
# fu = on
#                 abcdefghijklmnopqrstuvwxyz
adjustedAlphabet="aoeknltmfyqdzubpjgsxcvrhwi"
#                 awcdnlrmbyvkzfuojgsxeqthpi

#adjustedAlphabet=alphabet
file=open("crypt2.txt", "r")
content = file.read()
print(decodeSubst(content,adjustedAlphabet))
