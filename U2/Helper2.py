def isPrime(number):
    """
    is given number a prime number?
    this function returns True if so,
    otherwise false
    """
    # number must be greater than 1
    if (number<1):
        return False

    # check if number has no divisor other than itself (and one)
    for checkDivisor in range(2,number-1):
        if number % checkDivisor == 0:
            return False

    return True

def encrypt(zeichen,e,n):
    # ** entspricht ^
    cyphertext = (zeichen ** e) % n
    return cyphertext

def decrypt(cypher,d,n):
    plainText = (cypher ** d) % n
    return plainText

def encryptstring(text,e,n):
    enryptedText = []
    for zeichen in text:
        enryptedText.append(encrypt(ord(zeichen),e,n))
    return enryptedText

def decryotstring(cyphertext,d, n):
    plainText = ""
    for zeichen in cyphertext:
        plainText += chr((decrypt(zeichen,d,n)))
    return plainText