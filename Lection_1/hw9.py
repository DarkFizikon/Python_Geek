mounth = 12
salary_year = 0

for i in range(1,mounth + 1):
    salary = int(input(f"Salary in {i} mounth = "))
    salary_year += salary

avarage_salary = salary_year/mounth

print(f"The avarage salary for the year is: {avarage_salary}")