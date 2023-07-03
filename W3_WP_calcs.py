"""
Notes on Process of ROI calculation.
Functions to calculate total and validate input.
"""
#Return On Investment Calculator
#Four boxes

#Income: ie. $1000 rer month
    #Rental income , Launrdy income, storage income, etc. 
    #Total monthly income is total of incomes

#Expenses:
    #Taxes ie. $150pm
    #Insurance ie. $150pm
    #Utilities: Electric, Sewer, Electric, Gas 
    #HOA Fees 
    #Vacancy ie. 5% of Income
    #Repairs: Capital Expendature, etc. $100pm 
    #Property Manage: average 10% of Income
    #Mortgage: ie. avg. $860 pm
    #Total Monthly Expenses: $1610

#Cash Flow: Income - Expenses
    #Total: ie. $390

#Cash on Cash ROI(Return on Investment):
    #Down-Payment: ie $40,000
    #Closing Cost: ie $3000
    #Repair Cost: ie. $7000
    #Misc: ie $0
    #Total Investment: $50000
    #Annual Cash Flow: Cash Flow x 12: ie. $4,680
    #Cash on Cash ROI: Annual Cash Flow / Total Investment and return the percentage RETURN TOTAL

#Equity Calc?
import re 

def str_to_int(input):
    pattern = re.compile('^\$?([1-9]\d*\.?\d{0,2}$|^\$?0$|^\$?[1-9]\d{0,2}(,\d\d\d){0,4}(\.\d{0,2}$)?$)')
    string = pattern.search(input)
    if string:
        string = string.group(0)
        return string
    else:
        return 'Invalid Input'


def add_total(purchase, income, taxes, expenses):
    try:
        num_list = [purchase, income, taxes, expenses]
        for num in num_list:
            num_list[num_list.index(num)] = float(num.replace('$','').replace(',', ''))
        total_percentage = round((((((num_list[1] - num_list[3]) - num_list[2]) * 12) / num_list[0]) * 100) , 2)
        monthly_income = (num_list[1] - num_list[3]) - num_list[2]
        if total_percentage > 20:
            estimate = 'Great Investment'
        elif total_percentage > 10:
            estimate = 'Good Investment'
        elif total_percentage > 0:
            estimate = 'Mild Investment'
        else:
            estimate = 'Bad Investment'
        return (f"Total Investment Percentage: {total_percentage}%\nMonthly Income: ${monthly_income}\n{estimate}")
    except:
        return 'Invalid Input: Try Again'