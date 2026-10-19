message= input("Enter the coded text: ")
distance= int(input("Enter the distance value: "))

decrypted=""

for ch in message:
    decrypted += chr((ord(ch) - distance) % 128)


print(decrypted)