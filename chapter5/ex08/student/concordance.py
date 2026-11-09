def main():
filename = input("Enter the input file name: ")
 
word_counts = {}
 
try:
with open(filename, "r") as file:
for line in file:
words = line.split()
 
for word in words:
word = word.lower() # makes counting case-insensitive
 
if word in word_counts:
word_counts[word] += 1
else:
word_counts[word] = 1
 
for word in sorted(word_counts):
print(word, word_counts[word])
 
except FileNotFoundError:
print("File not found.")
 
main()