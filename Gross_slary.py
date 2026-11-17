# Calculate gross salary
def calculate_salary():
    basic_salary = 50000
    hra = basic_salary * 20 / 100
    da = basic_salary * 10 / 100

    gross_salary = basic_salary + hra + da

    print("Gross Salary:", gross_salary)


if __name__ == "__main__":
    calculate_salary()