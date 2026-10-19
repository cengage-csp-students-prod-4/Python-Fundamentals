message = input("Enter a message: ")
distance = int(input("Enter the distance value: "))

result = ""
for ch in message:
    result += chr((ord(ch) - 32 + distance) % 95 + 32)

print(result)