def caesar_chiper_encrypt(text, rot=5):
    result = ""
    text = text.lower()
    # For loop over every letter in the text
    for char in text:
        """
         ord converts char into ascii number (a = 97 / b = 98)
         Subtract 97  from ord so that a is 0 and b is 1 and so on.
         There for modulo works because only 0 to 25 works with this solution
        """
        # If its not a to z (97 to 122) just attach it to the string!
        if (ord(char) > 122 or ord(char) < 97):
            result += char
        else:
            ascii = (ord(char) - 97 + rot) % 26

            # Add 97 to get back into ascii Code and use chr to get back the enc letter
            resultchr = chr(ascii + 97)

            # Attach resultchr to result String
            result += resultchr
    return result


# result of function caesar_chiper_encrypt
enc = (caesar_chiper_encrypt("Hallo Duda !"))
print(enc)
# result of decription -5 to get the real text
dec = caesar_chiper_encrypt(enc, rot=-5)
print(dec)