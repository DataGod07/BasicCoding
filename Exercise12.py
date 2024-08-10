# Exercise 12: Calculate income tax for the given income by adhering to the rules below
salary = int(input('Enter Salary : '))
tax_amt = 0
tax_amt1 = 0
tax_amt2 = 0
tax_amt3 = 0
if salary>=10000:
    tax_amt1 = 10000*0
    salary = salary - 10000
    print(salary)
if salary>=10000:
    tax_amt2 = 10000 * 0.10
    salary = salary - 10000
    print(salary)
if salary>=10000:
    tax_amt3 = salary * 0.20
    print(salary)

print(tax_amt1+tax_amt2+tax_amt3)
