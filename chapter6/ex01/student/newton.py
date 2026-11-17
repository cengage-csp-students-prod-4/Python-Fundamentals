import math

def newton(x):
    """Returns the square root of x using Newton's method."""
    estimate = 1.0

    while True:
        new_estimate = (estimate + x / estimate) / 2

        if abs(new_estimate - estimate) < 0.000000001:
            return new_estimate

        estimate = new_estimate


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