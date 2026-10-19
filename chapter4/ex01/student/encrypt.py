message = input("Enter a message: ")
distance = int(input("Enter the distance value: "))
encrypted = ""

for ch in message:
    encrypted += chr(ord(ch) + distance)

print(encrypted)