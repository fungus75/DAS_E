# Basics
import random, math
from Helper import *

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
while gcd != 1:
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


ciphertext = encryptstring("Hallo abc",e,n)
print(ciphertext)

print(decryotstring(ciphertext,d,n))