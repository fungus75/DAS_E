from Helper import *

cyphernumbers = [68975, 21610, 30867, 30867, 38513, 3447, 20559, 31081, 6986,
                 38513, 59155, 42555, 20362, 38513, 40003, 53693, 42555,
                 50340, 17479, 38513, 33524, 11145, 25868]

publickey = [16439, 75839]

text = ""

# Pro Cyphernummer in Array
for cyphernumber in cyphernumbers:
    # In Bereich von Ascii 0 - 255
    for i in range(0, 255):
        # Falls encrypt gleich cyphernumber dann Zeichen in Text hinzufügen
        if encrypt(i, publickey[0], publickey[1]) == cyphernumber:
            text += chr(i)
            print(".")
            break
print(text)
