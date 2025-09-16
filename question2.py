# 2. Create a program whose major task is to calculate an individual’s Net Salary by getting the inputs basic salary and benefits. Calculate the payee (i.e. Tax), NHIFDeductions, NSSFDeductions, gross salary, and net salary.

# NB: Use KRA, NHIF, and NSSF values provided in the link below.
# https://www.aren.co.ke/payroll/taxrates.htm
# https://www.kra.go.ke/en/individual/calculate-tax/calculating-tax/paye

# MILESTONE TASK
# Create a class called Payroll whose major task is to calculate an individual’s Net Salary by getting the inputs basic salary and benefits. Create 5 different class methods which will calculate the payee (i.e. Tax), NHIFDeductions, NSSFDeductions, gross salary, and net salary.

#Instructions were to primarily make use of functions

salary = int(input("Enter your gross monthly salary: "))

def calculate_shif():
    #SHIF🤢
    shif = salary * 0.0275
    return shif

def calculate_nssf():
    nssf = salary * 0.06
    return nssf

def calculate_housing_levy():
    housing_levy = salary * 0.015
    return housing_levy

taxable_income = salary - (calculate_shif() + calculate_nssf() + calculate_housing_levy())

def calculate_payee():    
    #get the payee
    if taxable_income <= 24000:
        payee = taxable_income * 0.1
    elif taxable_income <= 32333:
        payee = taxable_income * 0.25
    elif taxable_income <= 500000:
        payee = taxable_income * 0.3
    elif taxable_income <= 800000:
        payee = taxable_income * 0.325
    elif taxable_income > 800000:
        payee = taxable_income * 0.35
    else:
        print("Enter a valid salary value")
    return payee



def calculate_net_salary():
    net_salary = salary -(calculate_payee() + calculate_shif() + calculate_nssf() + calculate_housing_levy())
    return print(f"Your net salary is: {net_salary}")

calculate_net_salary()