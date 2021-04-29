import math
import random

# this code is taken from our group work:
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
    for checkDivisor in range(2,number-1):     # int(math.sqrt(number)+1)
        if number % checkDivisor == 0:
            return False

    return True

# alle Primzahlen zwischen 0 und 500 finden und in ein Array schreiben
primes = [i for i in range(0,500) if isPrime(i)]

#random Primzahlen aus dem Array oben auswählen
p = random.choice(primes)
q = random.choice(primes)

# Prüfen, dass p nicht gleich q
while p == q:
    q = random.choice(primes)


n = p * q

#phi berechenen
phi = (p-1) * (q-1)

# gcd 2, damit start für while Schleife startet; Schleife läuft so lange, bis gcd von e und phi = 1
gcd = 2
while gcd != 1:  # when gcd is 1 the two are relativ prime to each other; gcd --> größter gemeinsamer Teiler
    e = random.randrange(1,phi)
    gcd = math.gcd(e,phi)


# modDE 2, damit in Schleife startet. Schleife läuft so lange bis passendes d gefunden.
modDE = 2
while modDE != 1:
    d = random.randrange(1,phi)
    de = d * e
    modDE = de % phi

# Testen der Decryot/Encrypt Funktionen aus dem Helper
print("publicKey: {",e,n,"}")
print("privateKey: {",d,n,"}")

# this is my addition:
# using this keys:
# public { 2973 87271 }
# private  { 36949 87271 }

encypted = encryptstring('200225',2973,87271)
print("Encrypted: ")
print(encypted)
decrypted= decryotstring(encypted,36949,87271)
print("Decrtyped:"+decrypted)