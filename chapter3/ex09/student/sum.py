sum = 0.0
count = 0
while True:
    Entry = input("Enter a number of press Enter to quit: ")
    if Entry == "":
        break
    sum += float(Entry)
    count += 1

if count > 0:
    average = sum/count

else:
    average = 0.0

print("The sum is", sum)
print("The average is", average)
