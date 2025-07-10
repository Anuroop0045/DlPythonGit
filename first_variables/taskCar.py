print("Calculate EMI of Mahindra Scorpio N")
'''
actual_price = 1726000
down_payment = 173000

bank_interest = 9.8
monthly_Intrest = float(bank_interest/12/100)

loanMonths = 4*12
loanAmount = actual_price-down_payment
intrest_Cal = float((loanAmount*monthly_Intrest*(1+monthly_Intrest)**loanMonths)/((1+monthly_Intrest)**loanMonths-1))
#loan_period = loanMonths

print(intrest_Cal)
'''
def emiCalculator(actualPrice: int, downPayment: int, yearlyIntrest: float, NumberOfYears: float):
    actual_price = actualPrice
    down_payment = downPayment

    bank_interest = float(yearlyIntrest)
    monthly_Intrest = float(bank_interest/12/100)

    loanMonths = NumberOfYears*12
    loanAmount = actual_price-down_payment
    emiPerMonth = float((loanAmount*monthly_Intrest*(1+monthly_Intrest)**loanMonths)/((1+monthly_Intrest)**loanMonths-1))
    return emiPerMonth


print(round(emiCalculator(1726297, 173000, 9.8, 4)))

