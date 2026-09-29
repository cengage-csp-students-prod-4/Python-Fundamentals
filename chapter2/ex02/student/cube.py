"""
Program: Cube Surface Area Calculator
Analysis:
This program calculates the surface area of a cube.
The user enters the edge of the cube as an integer.
The program uses the formula:
Surface Area = 6 * edge^2
The calculated surface area is then displayed with one decimal place.
Design:
1. Prompt the user to enter the length of a cube edge.
2. Calculate the surface area using:
surface_area = 6 * edge ** 2
3. Display the surface area with one decimal place.
"""
edge = int(input("Enter the cube's edge: "))

surface_area = 6 * edge ** 2

print(f"The surface area is  {surface_area:.1f}  square units.")