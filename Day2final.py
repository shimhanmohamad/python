print("Welcome to Tip Calculater")
bill = float(input("What was the total bill ? $"))
tip_perc = int(input("What percentage tip would you like to give ? 10,12 or 15 ? "))
people = int(input("How many people split the bill ? "))
perperson_total_bill = round(float((bill + (tip_perc/100)*bill)/people),2)
print(f"Each person shoul  pay : ${perperson_total_bill}")

