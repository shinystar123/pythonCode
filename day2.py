print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are splitting this bill? "))
tip_as_a_percent = tip/100
total_tip_amount = total_bill*tip_as_a_percent
bill = total_bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round()
calculations = (total_bill + (total_bill*tip)/100)/people
print("Each person should pay: " + round(calculations, 2))