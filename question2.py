# 2. Create a program whose major task is to calculate an individual’s Net Salary by getting the inputs basic salary and benefits. Calculate the payee (i.e. Tax), NHIFDeductions, NSSFDeductions, gross salary, and net salary.

# NB: Use KRA, NHIF, and NSSF values provided in the link below.
# https://www.aren.co.ke/payroll/taxrates.htm
# https://www.kra.go.ke/en/individual/calculate-tax/calculating-tax/paye

# MILESTONE TASK
# Create a class called Payroll whose major task is to calculate an individual’s Net Salary by getting the inputs basic salary and benefits. Create 5 different class methods which will calculate the payee (i.e. Tax), NHIFDeductions, NSSFDeductions, gross salary, and net salary.

#Instructions were to primarily make use of functions

basic_salary = float(input("Enter your gross monthly salary: "))
benefits = float(input("Enter your total benefits: "))
gross_salary = basic_salary + benefits




#SHIF
def calculate_shif():
    shif = gross_salary * 0.0275
    return shif

#going to assume tier 1 only for now
def calculate_nssf():
    if gross_salary <= 0:
        nssf = 0
    elif gross_salary <= 8000:
        nssf = gross_salary * 0.06
    else:
        nssf = 8000 * 0.06
    return nssf

def calculate_housing_levy():
    #Housing Levy🤮🤮🤮🤮
    housing_levy = gross_salary * 0.015
    return housing_levy

taxable_income = gross_salary - (calculate_shif() + calculate_nssf() + calculate_housing_levy())
def calculate_payee():    
    #get the payee
    if taxable_income <= 0:
        payee = 0
    elif taxable_income <= 24000:
        payee = taxable_income * 0.10
    elif taxable_income <= 32333:
        payee = (24000 * 0.10) + ((taxable_income - 24000) * 0.25)
    elif taxable_income <= 500000:
        payee = (24000 * 0.10) + ((32333 - 24000) * 0.25) + ((taxable_income - 32333) * 0.30)
    elif taxable_income <= 800000:
        payee = (24000 * 0.10) + ((32333 - 24000) * 0.25) + ((500000 - 32333) * 0.30) + ((taxable_income - 500000) * 0.325)
    else:
        payee = (24000 * 0.10) + ((32333 - 24000) * 0.25) + ((500000 - 32333) * 0.30) + ((800000 - 500000) * 0.325) + ((taxable_income - 800000) * 0.35)
    payee = payee - 2400
    if payee < 0:
        payee = 0
    return payee
    



def calculate_net_salary():
    net_salary = taxable_income - calculate_payee()
    return print(f"Your net salary is: {net_salary}")

calculate_net_salary()