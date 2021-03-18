from Helper import *

#enc=vigenere_encrypt("TRUEFRIENDs","BOOTS")
#print(enc)
#dec=vigenere_decrypt(enc,"BOOTS")
#print(dec)

#key=vigenere_getKey("TRUEFRIENDs","UFIXXSWSGVt")
#print(key)

printArray(findPairsInFile("crypt-small.txt", 3, 10))


relevantPart= getRelevantElementsInfile("crypt-small.txt")[0:7]
print(relevantPart)

#charStat=getCharStats("crypt.txt")


#positions=getCharIndexInStats(relevantPart,charStat)
#print(positions)

print("bnk: "+vigenere_getKey("the","bnk"))
print("ipk: "+vigenere_getKey("the","ipk"))
print("rtw: "+vigenere_getKey("the","rtw"))
print("fzt: "+vigenere_getKey("the","fzt"))
print("lwm: "+vigenere_getKey("the","lwm"))
print("znc: "+vigenere_getKey("the","znc"))
print("zfq: "+vigenere_getKey("the","zfq"))
print("pvj: "+vigenere_getKey("the","pvj"))
print("gtb: "+vigenere_getKey("the","gtb"))
print("mfs: "+vigenere_getKey("the","mfs"))


