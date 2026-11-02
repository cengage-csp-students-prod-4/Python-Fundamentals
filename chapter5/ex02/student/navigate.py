filename = input("Enter the input file name: ")

with open(filename, "r") as infile:
    lines = [line.rstrip("\n") for line in infile]

while True:
    print(f"The file has {len(lines)} lines.")
    line_num = int(input("Enter a line number [0 to quit]: "))

    if line_num == 0:
        break

    print(f"{line_num} :  {lines[line_num - 1]}")
    print()