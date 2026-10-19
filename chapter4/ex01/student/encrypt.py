message = input("Enter a message: ")
distance = int(input("Enter the distance value: "))

encrypted = ""

for ch in message:
    code = ord(ch)
    code = code + distance

    while code > 126:
        code = code - 95

    encrypted += chr(code)

print(encrypted)