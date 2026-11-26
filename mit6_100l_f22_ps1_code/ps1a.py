# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 14:56:20 2026

@author: ioseth

goal and learning:
using control flow in Python and formulating a computational solution to a problem.  
It will also give you a chance to explore bisection search
"""


def main():
    print('house hunting part A')
    
    #TODO: validate input to avoid strings 
    annual_salary =float(input("Enter your Annual salary (example 150000):"))
    portion_saved =float(input("Enter your portion of salary to be saved, as a decimal (example for 30% do: .3):"))
    total_cost    =float(input("Enter the cost of your Dream House: (example: 1000000)"))
    
    
    # annual_salary    = 75000
    # portion_saved    = .05
    # total_cost       = 1500000

    
    
    portion_down_payment = 0.25   #assuming 25% for simplicity 
    montly_salary        = annual_salary / 12
    annual_r_rate        = 0.04   # invesments earn a return of 4%

    
    month_count   =0    # 
    savings_sum   =0    # we'll start with 0 savings
    
    
    down_payment_total = portion_down_payment * total_cost


    while savings_sum < down_payment_total:
        savings_per_month_tmp =montly_salary*portion_saved
        
        roi_per_month         =savings_sum*annual_r_rate/12
        savings_sum           =savings_sum + (roi_per_month) + savings_per_month_tmp
        
        
        month_count +=1

    
    
    
    print("input data")
    print("salary:",annual_salary)
    print("savings:",portion_saved)
    print("cost of house:",total_cost)
    print("it'll take you ",month_count," months to cover the down payment")
    


if __name__ == '__main__':
    main()
    
    
    
    





