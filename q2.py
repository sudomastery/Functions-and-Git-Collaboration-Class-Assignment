def calculate_net_salary(basic_salary, benefits):
    # Gross salary = basic salary + benefits
    gross_salary = basic_salary + benefits

    # NSSF deduction (6% of basic up to a max of 2000)
    nssf_deduction = min(0.06 * basic_salary, 2000)

    # NHIF deduction (simplified example rates)
    if gross_salary <= 5999:
        nhif_deduction = 150
    elif gross_salary <= 7999:
        nhif_deduction = 300
    elif gross_salary <= 11999:
        nhif_deduction = 400
    elif gross_salary <= 14999:
        nhif_deduction = 500
    else:
        nhif_deduction = 600   # simplified flat rate

    # Taxable income = gross - NSSF
    taxable_income = gross_salary - nssf_deduction

    # PAYE Tax (simplified Kenyan bands)
    if taxable_income <= 24000:
        tax = 0.1 * taxable_income
    elif taxable_income <= 32333:
        tax = (0.1 * 24000) + (0.25 * (taxable_income - 24000))
    else:
        tax = (0.1 * 24000) + (0.25 * (32333 - 24000)) + (0.3 * (taxable_income - 32333))

    # Net salary
    net_salary = gross_salary - (tax + nhif_deduction + nssf_deduction)

    # Breakdown like a payslip
    print("\n--- Salary Breakdown ---")
    print(f"Basic Salary:           KES {basic_salary:,.2f}")
    print(f"Benefits:               KES {benefits:,.2f}")
    print(f"Gross Salary:           KES {gross_salary:,.2f}\n")

    print("--- Deductions ---")
    print(f"NSSF Deduction:         KES {nssf_deduction:,.2f}")
    print(f"NHIF Deduction:         KES {nhif_deduction:,.2f}")
    print(f"PAYE (Tax):             KES {tax:,.2f}\n")

    print(f"Net Salary (Take-home): KES {net_salary:,.2f}")
    print("--------------------------\n")
    print("Note: This is a simplified calculator. Actual NHIF & PAYE rates may differ slightly.\n")


# Example test
calculate_net_salary(50000, 10000)
