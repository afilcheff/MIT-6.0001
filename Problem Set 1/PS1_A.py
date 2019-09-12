annual_salary = int(input('Input your annual salary: '))
portion_saved = float(input('Input your portion of salary to be saved: '))
total_cost = int(input('Input the cost of your dream home: '))
portion_down_payment = 0.25
current_savings = 0
r = 0.04

downpayment = total_cost * portion_down_payment
monthly_salary = annual_salary / 12
amount_saved_per_month = monthly_salary * portion_saved
monthly_r = 0.04 / 12

months = 0

while not current_savings >= downpayment:
    current_savings *= (1 + (0.04/12))
    current_savings += amount_saved_per_month
    months += 1
    
print(months)
