# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 14:56:20 2026

@author: ioseth

goal and learning:
using control flow in Python and formulating a computational solution to a problem.  
It will also give you a chance to explore bisection search
"""


def main():
    
    print('house hunting part C')
    
    #TODO: validate input to avoid strings 
    annual_salary    =float(input("Enter the starting salary: "))

    
    
# Test Case 1
# Enter the starting salary:​ 150000 
# Best savings rate:​ 0.4411  
# Steps in bisection search:​ 12 
    #annual_salary    = 150000   
    
# Test Case 2 
# Enter the starting salary:​ 300000 
# Best savings rate:​ 0.2206 
# Steps in bisection search:​ 9 
    #annual_salary    = 300000  

# Test Case 3 
# Enter the starting salary:​ 10000 
# It is not possible to pay the down payment in three years. 
    # annual_salary    = 10000  
    
    portion_saved =0
    total_cost       = 1000000   # assume the cost of the house is $1M
    semi_annual_raise= .07       # assume semi-annual raise of 7%
    number_of_months = 36        # period of time to find best savings rate 
    down_payment_percentage = 0.25  ## assuming 25% for simplicity 
    annual_r_rate           = 0.04  ## your 'invesments will retunr 4%
    
    montly_salary           = annual_salary / 12
    
    
    down_payment_total = down_payment_percentage * total_cost
    
    ## salary after 6, 12, 18 and so on months
    savings_per_month=[]
    month_count   =0
    month_counter =0    
    savings_sum   =0
    steps_in_bisection=0
    ## savings_sum_year=0
    semesterA=True
    salary_in_current_semester=montly_salary
    savings_per_bisection=[]
    
    a=0
    b=10000 if montly_salary >= 10000 else montly_salary
    c=(a+b)/2;
    portion_saved=c/float(montly_salary)
    enough_savings=False
    cant_save_enough_36months=False
    months_36_done=False
    bisection_limit=False
        
    while  enough_savings == False and cant_save_enough_36months == False:
        
        while months_36_done ==False and month_counter < 6 and enough_savings==False:
            savings_per_month_tmp =salary_in_current_semester*portion_saved
            ## savings_sum_year = savings_sum_year + savings_per_month_tmp
            roi_per_month         =savings_sum*annual_r_rate/12
            savings_sum           =savings_sum + (roi_per_month+savings_per_month_tmp)
            savings_per_month.append(roi_per_month+savings_per_month_tmp)
            month_count +=1
            month_counter +=1
            
            if savings_sum >= down_payment_total:
                enough_savings = True
        
        if month_count >= number_of_months:
            months_36_done = True
        
            
        salary_in_current_semester=salary_in_current_semester+salary_in_current_semester*semi_annual_raise
        ## savings_sum_year=0 if not(semesterA) else savings_sum_year
        semesterA=not(semesterA)
        month_counter=0
        

                
        if months_36_done and enough_savings==False and bisection_limit==False:
                    a=c
                    c=(a+b)/2;
                    portion_saved=float(c/montly_salary)
                    steps_in_bisection +=1
                    print(abs(a -b), "portions saved")
                    if abs(a - b) <=100:
                        bisection_limit =True
                        
        if months_36_done and enough_savings==False and bisection_limit==True:
            cant_save_enough_36months = True
                        
        if months_36_done: ## reset state for new bisection run
                savings_per_month=[]
                month_count   =0
                month_counter =0 
                savings_per_bisection.append(savings_sum)
                savings_sum   =0
                salary_in_current_semester=montly_salary
                months_36_done = False

    
    for i in savings_per_bisection:
        print("savings per bisection ",i)

    if  enough_savings == True:
        print("down payment total",down_payment_total)
        print("salary:",annual_salary)
        print("savings:",savings_sum)
        print("steps_in_bisection",steps_in_bisection)
        print("it'll take you ",month_count," months to cover the down payment")
        print("best percentage saving ",portion_saved)
    else:
        print("it is no t possible to pay the down payment in three years")
        print("down payment total",down_payment_total)
        print("salary:",annual_salary)
        print("savings:",savings_sum)
        print("steps_in_bisection",steps_in_bisection)
        print("it'll take you ",month_count," months to cover the down payment")
        print("best percentage saving ",portion_saved)

if __name__ == '__main__':
    main()





    
