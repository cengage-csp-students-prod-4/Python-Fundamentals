salary = float(input("Enter the starting salary: "))
increase = float(input("Enter the annual % increase: "))
years_amount = int(input("Enter the number of years: "))

print("Year Salary")
print("-------------")

for year in range(1, years_amount + 1):
    print(f"{year:>2} {salary:.2f}")
    salary = salary * (1 + increase / 100)