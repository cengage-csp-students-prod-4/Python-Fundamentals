message = input("Enter a message: ")
distance = int(input("Enter the distance value: "))

encrypted = ""

for ch in message:
    if 32 <= ord(ch) <= 126:
        new_code = ((ord(ch) - 32 + distance) % 95) + 32
        encrypted += chr(new_code)
    else:
        encrypted += ch

print(encrypted)