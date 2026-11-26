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
    # annual_salary    =float(input("Enter your Annual salary: "))
    # portion_saved    =float(input("Enter your percent to be saved: "))
    # total_cost       =float(input("Enter the cost of your Dream House: "))
    # semi_annual_raise=float(input("Enter your raise percentage in decimals for every 6 months: "))
    # number_of_months =int(input("Enter the number of months: "))
    
    
    annual_salary    = 1200
    portion_saved    = .2
    total_cost       = 8000000
    semi_annual_raise= .01
    number_of_months = 36
    
    down_payment_percentage = 0.25  ## assuming 25% for simplicity 
    current_savings         = 0     ## we'll start with 0 savings
    annual_r_rate           = 0.04  ## your 'invesments will retunr 4%
    montly_salary           = annual_salary / 12
    
    
    down_payment_total = down_payment_percentage * total_cost
    
    ## salary after 6, 12, 18 and so on months
    salary_increments=number_of_months/6 + (1 if (number_of_months % 12 > 0) else 0 ) - 1 ##number of semesters
    
    salary_per_semester=[montly_salary]
    savings_per_semester =[montly_salary*portion_saved]
    new_montly_salary  = 0
    
    for element_tmp in range(int(salary_increments)):
        new_montly_salary = salary_per_semester[element_tmp] + (salary_per_semester[element_tmp]*semi_annual_raise)
        salary_per_semester.append(new_montly_salary)
    
    #for i in salary_per_semester:
    #    print("salary per semster: ", i)        
    
    salary_per_year=[]
    savings_per_year=[]
    annual_roi_per_semester=[]
    ## bi semestral computation
    partial_year     = number_of_months%12
    partial_semester = number_of_months%6
    years_of_salary  = number_of_months/12

   
# %%
#     print(salary_increments, "salary_increments")
#     print("partial semester",partial_semester)
    
#     print(len(salary_per_semester) - 1 ,"while loop")
    
#     print((len(salary_per_semester))%2,"while loop2")
    
#     for i in salary_per_semester:
#         print("salary_per_semester",salary_per_semester)
    
#     semester_num=0
#     while semester_num < (len(salary_per_semester) - 2):      ## iterating before the last 2 elements to later evaluate odd num of semesters
#         salary_per_year_tmp = 0;
#         salary_per_year_tmp = salary_per_year_tmp + salary_per_semester[semester_num]*6
#         salary_per_year_tmp = salary_per_year_tmp + salary_per_semester[semester_num+1]*6
#         salary_per_year.append(salary_per_year_tmp)
#         semester_num +=2
 
#     ## checking for months  lower than 6 , or higher than 6
#     if int(len(salary_per_semester))%2 ==0 and partial_year == 0:       ## pair number of full semesters
#         salary_per_year_tmp = 0;
#         salary_per_year_tmp = salary_per_year_tmp + salary_per_semester[semester_num]*6
#         salary_per_year_tmp = salary_per_year_tmp + salary_per_semester[semester_num+1]*6
#         salary_per_year.append(salary_per_year_tmp)
#         print("even number of full semesters")
#     elif int(len(salary_per_semester))%2 ==0 and partial_semester > 0:  ## full semester plus partial semester
#         salary_per_year_tmp = 0;
#         salary_per_year_tmp = salary_per_year_tmp + salary_per_semester[semester_num]*6
#         salary_per_year_tmp = salary_per_year_tmp + salary_per_semester[semester_num+1]*partial_semester
#         salary_per_year.append(salary_per_year_tmp)
#         print("even num of semesters with partial months")
#     else:                                                               ## partial semester less than 6 months 
#         salary_per_year_tmp = 0;
#         salary_per_year_tmp = salary_per_year_tmp + salary_per_semester[semester_num]*partial_year ## using partial year because , module 6 yields 0 withh odd number of semesters too eg 18 months is 3 semesters , 18 mod 6 = 0
#         salary_per_year.append(salary_per_year_tmp)
#         print("1 semester partial months only")



# #############savings per semester 
#     semester_num=0
#     while semester_num < (len(salary_per_semester) - 2):      ## iterating before the last 2 elements to later evaluate odd num of semesters
#         savings_per_semester1 = 0
#         savings_per_semester2 = 0        
#         roi_semester1=0
#         roi_semester2=0
#         savings_per_semester1 = salary_per_semester[semester_num]*6*portion_saved
#         roi_semester1=savings_per_semester1*annual_r_rate;
#         annual_roi_per_semester.append(roi_semester1)
        
        
#         savings_per_semester2 = salary_per_semester[semester_num+1]*6*portion_saved
#         roi_semester2=savings_per_semester2*annual_r_rate;
#         savings_per_semester.append(savings_per_semester1)
        
        
#         savings_per_semester.append(savings_per_semester2)
#         annual_roi_per_semester.append(roi_semester2)
#         semester_num +=2
 
#     ## checking for months  lower than 6 , or higher than 6
#     if int(len(salary_per_semester))%2 ==0 and partial_year == 0:       ## pair number of full semesters
#         savings_per_semester1 = 0
#         savings_per_semester2 = 0        
#         roi_semester1=0
#         roi_semester2=0
#         savings_per_semester1 = salary_per_semester[semester_num]*6*portion_saved
#         roi_semester1=savings_per_semester1*annual_r_rate;
#         annual_roi_per_semester.append(roi_semester1)        
#         savings_per_semester2 = salary_per_semester[semester_num+1]*6*portion_saved
#         roi_semester2=savings_per_semester2*annual_r_rate;
#         savings_per_semester.append(savings_per_semester1)
#         savings_per_semester.append(savings_per_semester2)
#         annual_roi_per_semester.append(roi_semester2)
#         print("even number of full semesters")
#     elif int(len(salary_per_semester))%2 ==0 and partial_semester > 0:  ## full semester plus partial semester
#         savings_per_semester1 = 0
#         savings_per_semester2 = 0        
#         roi_semester1=0
#         roi_semester2=0
#         savings_per_semester1 = savings_per_semester1[semester_num]*6*portion_saved
#         roi_semester1=savings_per_semester1*annual_r_rate;
#         annual_roi_per_semester.append(roi_semester1)        
#         savings_per_semester2 = salary_per_semester[semester_num+1]*partial_semester*portion_saved
#         roi_semester2=savings_per_semester2*annual_r_rate;
#         savings_per_semester.append(savings_per_semester1)
#         savings_per_semester.append(savings_per_semester2)
#         annual_roi_per_semester.append(roi_semester2)       
#         print("even num of semesters with partial months")
#     else:                                                               ## partial semester less than 6 months 
#         savings_per_semester1 = 0        
#         roi_semester1=0
#         savings_per_semester1 = salary_per_semester[semester_num]*partial_semester*portion_saved
#         roi_semester1=savings_per_semester1*annual_r_rate;
#         annual_roi_per_semester.append(roi_semester1)        
#         savings_per_semester.append(savings_per_semester1)              
#         print("1 semester partial months only")
# %%

        
    # for k in salary_per_year:
    #     print("salary_per_year",k)

    # for i in savings_per_semester:
    #     print("savings_per_year",i)
        
    # for j in annual_roi_per_semester:
    #      print("roi_per_year",j)
         
    
        
    savings_per_month=[]
    semester_num=0
    month_count =0
    month_counter =0    
    savings_sum =0

    savings_per_semester1 = 0
    savings_per_semester2 = 0        
    roi_semester1=0
    roi_semester2=0
    semesterA    =True
    salary_per_semester=montly_salary
    
    while savings_sum < down_payment_total:
        while month_counter < 6 and savings_sum < down_payment_total:
            savings_per_month_tmp =salary_per_semester*portion_saved
            roi_per_month         =savings_per_month_tmp*annual_r_rate/12
            savings_sum           =savings_sum + (roi_per_month+savings_per_month_tmp)
            savings_per_month.append(roi_per_month+savings_per_month_tmp)
            month_count +=1
            month_counter +=1
            print("mont count",month_count)
        salary_per_semester=salary_per_semester+salary_per_semester*semi_annual_raise
        month_counter=0



    print("input data")
    print("salary:",annual_salary)
    print("savings:",portion_saved)
    print("cost of house:",total_cost)
     


if __name__ == '__main__':
    main()





    
