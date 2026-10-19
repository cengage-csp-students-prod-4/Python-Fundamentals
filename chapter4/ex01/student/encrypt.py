message = input("Enter a message: ")
distance = int(input("Enter the distance value: "))
 
result = ""
for ch in message:
    result += chr((ord(ch) + distance) % 128)
 
print(result)