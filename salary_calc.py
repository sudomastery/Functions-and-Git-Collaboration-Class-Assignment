
basic_salary=float(input("Enter basic salary: "))
benefits=float(input("Enter benefits: "))

# function to calculate gross salary
def calculate_gross_salary(basic_salary, benefits):
    return basic_salary+benefits

# NSSF deduction
def calculate_nssf_deduction(gross_salary):
    pensionable_pay=min(gross_salary,72000)
    return pensionable_pay*0.06

# SHIF deduction
def calculate_shif_deduction(gross_salary):
    return gross_salary*0.0275

# paye
def calculate_paye(gross_salary,nssf,shif):
    taxable_income=gross_salary-nssf-shif
    if taxable_income<=24000:
        paye=taxable_income*0.10
    elif taxable_income<=32333:
        paye=(24000*0.10)+((taxable_income-24000)*0.25)
    elif taxable_income<=500000:
        paye=(24000*0.10)+(32333-24000)*0.25+((taxable_income-32333)*0.30)
    elif taxable_income<=800000:
        paye=(24000*0.10)+(32333-24000)*0.25+(500000-32333)*0.30+((taxable_income-500000)*0.325)
    else:
        paye=(24000*0.10)+((32333-24000)*0.25)+((500000-32333)*0.30)+((800000-500000)*0.325)+((taxable_income-800000)*0.35)
# personal relief calc
    personal_relief=2400
    return max(paye-personal_relief, 0)

def calculate_net_salary(gross_salary,nssf,shif,paye):
    return gross_salary-nssf-shif-paye

gross_salary=calculate_gross_salary(basic_salary, benefits)
nssf=calculate_nssf_deduction(gross_salary)
shif=calculate_shif_deduction(gross_salary)
paye=calculate_paye(gross_salary,nssf,shif)
net_salary=calculate_net_salary(gross_salary,nssf,shif,paye)

print(f'Gross salary:{gross_salary:.2f}')
print(f'NSSF Deduction:{nssf:.2f}')
print(f'SHIF Deduction:{shif:.2f}')
print(f'PAYE:{paye:.2f}')
print(f'Net Salary:{net_salary:.2f}')

