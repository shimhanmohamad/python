# print("Welcome to life time checker!!!!")
# age=int(input("What is your current age : "))
# #let assume your maximum life time is 90 years
# life_time_left=90 - age
# leftdays=life_time_left*365
# leftweeks=life_time_left*52
# leftmonths=life_time_left*12
# print(f"you have {leftdays} days,{leftweeks} weeks,{leftmonths} months left")
print("Welcome to the tip calculater")

bill=float(input("What was the final bill ?$ "))
tip=int(input("what percentage would you like to tip? 10,12 or 15 ?"))
total_bill=bill+(tip/100)*bill
people=int(input("how many people split for this bill ?  "))
each_person_bill=float(total_bill)/people
final_amount_perperson=round (each_person_bill,2)
print(f"Each person should pay :${final_amount_perperson}")


      

