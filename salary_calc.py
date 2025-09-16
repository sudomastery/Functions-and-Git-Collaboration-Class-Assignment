# basic salary input by user
basic_salary=float(input('Enter your basic salary (Ksh): '))
# user enters their benefits
benefits=float(input('Enter your benefits (Ksh): '))

# calculate gross salary
gross_salary=basic_salary+benefits

# print the gross salary
print(f'Gross salary: Ksh {gross_salary:.2f}')

# NSSF deduction
nssf_pensionable_salary=min(gross_salary,72000)
nssf_deduction=nssf_pensionable_salary*0.06
print(f'NSSF Deduction: Ksh {nssf_deduction:.2f}')

# SHIF deduction
shif_deduction=gross_salary*0.0275
print(f'SHIF Deduction: Ksh{shif_deduction:.2f}')

# paye calculation

taxable_income=gross_salary-nssf_deduction-shif_deduction

# paye

if taxable_income<=24000:
    paye=taxable_income * 0.10
elif taxable_income<=32333:
    paye=(24000*0.10)+((taxable_income-24000))*0.25
elif taxable_income<=500000:
    paye=(24000*0.10)+((32333-24000)*0.25)+((taxable_income-32333)*0.30)
elif taxable_income<=800000:
    paye=(24000*0.10)+((32333-24000)*0.25)+((50000-32333)*0.30)+((taxable_income-50000)*0.35)
else:
    paye=(24000*0.10)+((32333-24000)*0.25)+((50000-32333)*0.30)+((80000-50000)*0.35)+((taxable_income-80000)*0.37)

# personal relief calc
personal_relief=2400
paye=max(paye-personal_relief,0)

print(f'PAYE: Ksh{paye:.2f}')