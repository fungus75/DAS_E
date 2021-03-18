from U1.Helper1 import *
from U2.Helper2 import *
import random

# 65 -90 Grossbuchstaben
key = ""
for i in range(0, 10):
    key += chr(random.randrange(65, 90))
text = """The Project Gutenberg EBook of The Adventures of Sherlock Holmes
by Sir Arthur Conan Doyle
(#15 in our series by Sir Arthur Conan Doyle)

Copyright laws are changing all over the world. Be sure to check the
copyright laws for your country before downloading or redistributing
this or any other Project Gutenberg eBook.

This header should be the first thing seen when viewing this Project
Gutenberg file.  Please do not remove it.  Do not change or edit the
header without written permission.

Please read the "legal small print," and other information about the
eBook and Project Gutenberg at the bottom of this file.  Included is
important information about your specific rights and restrictions in
how the file may be used.  You can also find out about how to make a
donation to Project Gutenberg, and how to get involved."""

# Wir sind Alice
# Bobs Public key ist 4029, 14809
cypher = vigenere_encrypt(text, key)
print(cypher)

encryptedkey = encryptstring(key, 4029, 14809)
print(encryptedkey)

# Wir sind Bob
# Unser Privat Key ist 8569, 14809
decryptedKey = decryotstring(encryptedkey, 8569, 14809)
print(decryptedKey)
plainttext = vigenere_decrypt(cypher,decryptedKey)
print(plainttext)