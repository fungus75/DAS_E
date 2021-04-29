# DAS E Exam 15.04.2021
# Inputs:
# has = Sum of ASCI Codes of all characters
original_message = "Fabulous!"
signature = 87236
privateKey = (294767, 698069)
publicKey = (971, 698069)

def decrypt(cypher,d,n):
    plainText = (cypher ** d) % n
    return plainText

#decrypt with public key
decryptedSignature = decrypt(signature,971,698069)
print(decryptedSignature)

# --> hash is 399654 not the same --> inorrect

if decryptedSignature == 866:
    print("signature correct")
else:
    print("signature not correct")