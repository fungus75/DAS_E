import base64

# it is line 152
# 4.2.9. Pre-Shared Key Exchange Modes ......................51
base64_message = 'ICAgICAgICAgICA0LjIuOS4gUHJlLVNoYXJlZCBLZXkgRXhjaGFuZ2UgTW9kZXMgLi4uLi4uLi4uLi4uLi4uLi4uLi4uLjUxCg=='
base64_bytes = base64_message.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('ascii')

print(base64_message)
print(base64_bytes)
print(message_bytes)
print(message)

# Variable
searchmessage = message
# Counter for line and normal count of String
linecounter = 0
count = 0
# Open file
file = open("rfc8446.txt", "r")
# read file per line
for line in file:
    # linecounter + 1 for each line
    linecounter += 1
    message = line
    # encode text
    message_bytes = message.encode('ascii')
    # convert letter in bytes
    base64_bytes = base64.b64encode(message_bytes)
    # decode bytes to string
    base64_message = base64_bytes.decode('ascii')

    print(" Message " + message)
    print(message_bytes)
    print(base64_bytes)
    print(" base64 Message " +base64_message)

    # compre file if its starts with ICAgQ if yes +1
    if base64_message.startswith("ICAgQ"):
        count += 1

    # if searchmessage is same as line then print out the line number
    if searchmessage == line:
        print("Found in line: " + str(linecounter))

print("Amout of lines that starting with ICAgQ " + str(count))