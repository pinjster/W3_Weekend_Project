"""
GUI Tkinter ROI Calculator.
Run first. Contains Inputs class.
Takes input from user and verifies it.
Get Total Btn adds up total and returns Total Investment Percentage and Monthly Income.
Adjusts when user changes screen size.
"""
from tkinter import *
from W3_WP_calcs import str_to_int as sti , add_total

class Inputs():
    def __init__(self, row, column, name, prompt):
        self.name = name
        self.row_start = row
        self.column_start = column
        self.prompt = prompt
        self.layout()

    def layout(self):
        self.label = Label(window, text=self.prompt)
        self.txt = StringVar(window, value='$')
        self.textbox = Entry(window , textvariable= self.txt, width= 35)
        self.textbox.bind('<Return>', self.clicked)
        self.enter_btn = Button(window, text="Enter", command=self.clicked, bg='darkgrey', fg='white')
        self.clear_btn = Button(window, text="Clear", command=self.clear, bg='darkgrey', fg='white')
        self.valid = Label(window, text='')
        self.label.grid(row=self.row_start,column=self.column_start, sticky=W)
        self.textbox.grid(row=self.row_start+1,column=self.column_start)
        self.enter_btn.grid(row=self.row_start+1,column=self.column_start + 1, sticky=W)
        self.clear_btn.grid(row=self.row_start+1,column=self.column_start + 2, sticky=W)
        self.valid.grid(row=self.row_start + 2,column=self.column_start, pady=5)

    def clicked(self, event=''):
        val = sti(self.txt.get())
        self.valid.configure(text=val, fg='black')
        self.txt.set(val)
        if val == 'Invalid Input':
            self.valid.configure(fg='red')

    def clear(self):
        self.txt.set('$')
        self.valid.configure(text='')

def get_total():
    return_val = add_total(input1.txt.get(), input2.txt.get(), input3.txt.get(), input4.txt.get())
    if return_val == 'Invalid Input: Try Again':
        total_print.config(fg='red')
    else:
        total_print.config(text=return_val, fg='black')

window = Tk()
window.title('ROI Calculator')
window.geometry('400x600')

title = Label(window, text="ROI Calculator for\nEstate-to-Rental Properties", pady=20)

#input 1:Purchase Price
input1 = Inputs(2,1,'purchase_price', "Enter Estate Purchase Price:\n(Include Additional Repairs)")

#input 2: Expected Rental Income
input2 = Inputs(5,1,'rental_income', "Enter Expected Monthly Rental Income:")

#input 3: Property Taxes
input3 = Inputs(8,1,'property_taxes', "Enter Monthly Property Taxes:")

#input 4: Maintenance Expenses
input4 = Inputs(11,1,'maintenance_expenses',"Enter Monthly Maintenance Expenses:")

#Total Button / Results
total_btn = Button(window, text="Get Total", command=get_total, width=30, bg='darkgrey')
total_print = Label(window, text="", pady=20)

window.columnconfigure(0, weight=1, minsize=5)
window.columnconfigure(5, weight=1, minsize=5)
title.grid(row=0,column=1,sticky=NE)
total_btn.grid(row=15,column=1)
total_print.grid(row=16,column=1)

window.mainloop()