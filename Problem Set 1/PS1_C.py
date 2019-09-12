#guessing the best savings rate given some conditions in order to save an amount for a house, using 'bisection search' algorithm

year_salary = int(input('Input yearly salary: '))
semi_annual_raise = 0.07
cost_house = 1000000
downpayment = 0.25 * cost_house
months = 36

low = 0.0
x = 1
high = x
guess = (high + low)/2.0
current_savings = 0
amount_saved_per_month = year_salary / 12 * guess
counter = 0

while abs(current_savings - downpayment) >= 100:
    current_savings = 0
    for i in range (1, months + 1):
        current_savings *= (1 + (0.04/12))
        current_savings += amount_saved_per_month
        if i % 6 == 0:
            amount_saved_per_month *= (1 + semi_annual_raise)
    if current_savings < downpayment:
        low = guess
    else:
        high = guess
        
    guess = (high + low)/2.0
    amount_saved_per_month = year_salary / 12 * guess
    counter += 1
    if abs(current_savings - downpayment) <= 100:
        print('Best savings rate: ', round(guess))
    else:
        if low == high:
            print('It is not possible to pay the down payment in three years.')
            break
