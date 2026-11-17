import math

def newton(x):
    estimate = 1.0
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - estimate ** 2)
        if difference <= 0.000001:
            break
    return estimate


def main():
    while True:
        data = input("Enter a positive number or enter/return to quit: ")

        if data == "":
            break

        number = float(data)

        print("The program's estimate is", newton(number))
        print("Python's estimate is     ", math.sqrt(number))


if __name__ == "__main__":
    main()