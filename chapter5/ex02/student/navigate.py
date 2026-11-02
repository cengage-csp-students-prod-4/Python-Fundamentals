def main():
    filename = input("Enter the input file name: ")

    with open(filename, "r") as f:
        lines = f.readlines()

    count = len(lines)

    while True:
        print("The file has " + str(count) + " lines.")
        number = int(input("Enter a line number [0 to quit]: "))

        if number == 0:
            break

        if 1 <= number <= count:
            print(number, ": ", lines[number - 1])
        else:
            print("Line number must be between 1 and " + str(count) + ".\n")
