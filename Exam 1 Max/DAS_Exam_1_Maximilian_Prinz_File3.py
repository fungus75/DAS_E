# DAS E Exam 15.04.2021
# Inputs:
# has = Sum of ASCI Codes of all characters
original_message = "Fabulous!"
signature = 87236
privateKey = (294767, 698069)
publicKey = (971, 698069)

# Generate has
hash = 0
for i in original_message:
    asciValue = ord(i)
    hash += asciValue

print(str(hash))
