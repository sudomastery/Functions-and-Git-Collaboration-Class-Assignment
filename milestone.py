# The Payroll class is defined and is an example of encapsulation
class Payroll:
    # Constructor to initialize the class with basic salary and benefits
    def __init__(self, basic_salary, benefits):
        self.basic_salary = basic_salary
        self.benefits = benefits

    # Method to calculate the gross salary
    def calculate_gross_salary(self):
        return self.basic_salary + self.benefits

    # Method to calculate NSSF deductions (2025 rates)
    def calculate_nssf_deductions(self):
        gross_salary = self.calculate_gross_salary()
        tier1 = min(gross_salary, 8000) * 0.06
        tier2 = 0
        if gross_salary > 8000:
            tier2 = min(gross_salary - 8000, 72000 - 8000) * 0.06
        return tier1 + tier2

    # Method to calculate SHIF deduction (2.75% of gross)
    def calculate_shif_deductions(self):
        gross_salary = self.calculate_gross_salary()
        return gross_salary * 0.0275

    # Method to calculate Housing Levy (1.5% of gross)
    def calculate_housing_levy(self):
        gross_salary = self.calculate_gross_salary()
        return gross_salary * 0.015

    # Method to calculate PAYE (tax)
    def calculate_payee(self):
        gross_salary = self.calculate_gross_salary()
        nssf = self.calculate_nssf_deductions()
        shif = self.calculate_shif_deductions()
        housing = self.calculate_housing_levy()
        taxable_income = gross_salary - nssf - shif - housing

        payee_rates = [
            (24000, 0.10),
            (32333, 0.25),
            (500000, 0.30),
            (800000, 0.325),
            (float('inf'), 0.35)  # meaning any amount >800,000
        ]

        tax = 0
        prev_limit = 0
        for limit, rate in payee_rates:
            if taxable_income > limit:
                tax += (limit - prev_limit) * rate
                prev_limit = limit
            else:
                tax += (taxable_income - prev_limit) * rate
                break
        tax -= 2400  # Personal relief
        return max(tax, 0)

    # Method to calculate net salary
    def calculate_net_salary(self):
        gross_salary = self.calculate_gross_salary()
        nssf = self.calculate_nssf_deductions()
        shif = self.calculate_shif_deductions()
        housing = self.calculate_housing_levy()
        payee = self.calculate_payee()
        total_deductions = nssf + shif + housing + payee
        return gross_salary - total_deductions

if __name__ == '__main__':
    basic_salary = float(input("Enter the basic salary: "))
    benefits = float(input("Enter the benefits: "))
    payroll = Payroll(basic_salary, benefits)
    print(f"Gross Salary: {payroll.calculate_gross_salary():.2f}")
    print(f"NSSF Deductions: {payroll.calculate_nssf_deductions():.2f}")
    print(f"SHIF Deductions: {payroll.calculate_shif_deductions():.2f}")
    print(f"Housing Levy: {payroll.calculate_housing_levy():.2f}")
    print(f"PAYE: {payroll.calculate_payee():.2f}")
    print(f"Net Salary: {payroll.calculate_net_salary():.2f}")