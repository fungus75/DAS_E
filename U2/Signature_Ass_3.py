from U1.Helper1 import *
from U2.Helper2 import *
import random
import hashlib

text = """Fabulous!"""

# Wir sind Alice
# Alice Private Key ist 175, 66767
hashvalue = str(hashlib.md5(text.encode()).hexdigest())
signature = encryptstring(hashvalue, 294767, 698069)
# Drucke Signature von Alice
print(signature)
print("Certificate: ", 43135, 66767)

# Wir sind Bob
hashAlice = decryotstring(signature, 971, 698069)
hashBob = str(hashlib.md5(text.encode()).hexdigest())

if hashAlice == hashBob:
    print("Das Zertifikat ist gültig.")

print(hashBob)
