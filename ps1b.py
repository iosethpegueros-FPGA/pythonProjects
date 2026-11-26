# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 14:56:20 2026

@author: ioseth

goal and learning:
using control flow in Python and formulating a computational solution to a problem.  
It will also give you a chance to explore bisection search
"""


def main():
    
    print('house hunting part B')
    
    #TODO: validate input to avoid strings 
    annual_salary    =float(input("Enter your Annual salary: "))
    portion_saved    =float(input("Enter your percent to be saved: "))
    total_cost       =float(input("Enter the cost of your Dream House: "))
    semi_annual_raise=float(input("Enter your raise percentage in decimals for every 6 months: "))
    
    # annual_salary    = 75000
    # portion_saved    = .05
    # total_cost       = 1500000
    # semi_annual_raise= .05
    
    down_payment_percentage = 0.25  ## assuming 25% for simplicity 
    annual_r_rate           = 0.04  ## your 'invesments will retunr 4%
    montly_salary           = annual_salary / 12
    
    
    down_payment_total = down_payment_percentage * total_cost
    
    ## salary after 6, 12, 18 and so on months
    savings_per_month=[]
    month_count   =0
    month_counter =0    
    savings_sum   =0

    semesterA=True
    salary_in_current_semester=montly_salary
    
    while savings_sum < down_payment_total:
        while month_counter < 6 and savings_sum < down_payment_total:
            savings_per_month_tmp =salary_in_current_semester*portion_saved
            roi_per_month         =savings_sum*annual_r_rate/12
            savings_sum           =savings_sum + (roi_per_month+savings_per_month_tmp)
            savings_per_month.append(roi_per_month+savings_per_month_tmp)
            
            month_count +=1
            month_counter +=1
        salary_in_current_semester=salary_in_current_semester+salary_in_current_semester*semi_annual_raise
        month_counter=0

 
    print("down payment total",down_payment_total)
    print("salary:",annual_salary)
    print("savings:",savings_sum)
    print("down_payment:",down_payment_total)
    print("semin annual raise:",semi_annual_raise)
    print("it'll take you ",month_count," months to cover the down payment")
     


if __name__ == '__main__':
    main()





    
