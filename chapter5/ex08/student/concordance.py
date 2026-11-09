filename = input("Enter the input file name: ")

counts = {}

with open(filename, "r") as infile:
    for line in infile:
        words = line.split()

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

for word in sorted(counts):
    print(word, counts[word])