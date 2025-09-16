# basic salary input by user
basic_salary=float(input('Enter your basic salary (Ksh): '))
# user enters their benefits
benefits=float(input('Enter your benefits (Ksh): '))

# calculate gross salary
gross_salary=basic_salary+benefits

# print the gross salary
print(f'Gross salary: Ksh {gross_salary:.2f}')