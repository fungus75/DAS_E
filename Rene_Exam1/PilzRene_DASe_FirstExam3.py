
# taken from sample 1 or from our group-work
def encrypt(zeichen,e,n):
    # ** entspricht ^
    cyphertext = (zeichen ** e) % n
    return cyphertext

def decrypt(cypher,d,n):
    plainText = (cypher ** d) % n
    return plainText



# my code during exam:
message = "Fabulous!"

def simpleHash(text):
    hash=0
    for char in text:
        hash += ord(char)
    return hash

def verifySignature(encSig,hash,e,n):
    decryptedHash=decrypt(encSig,e,n)
    if decryptedHash == hash:
        return True
    else:
        return False

hash = simpleHash(message)
print("Hash of message "+message+" is: ",hash)
print("Signature 87236 is valid: ", verifySignature(87236,hash,971,698069))

print(encrypt(866,294767,698069))