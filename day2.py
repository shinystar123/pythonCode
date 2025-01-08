print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people are splitting this bill? ")
calculations = (total_bill + (total_bill*tip)/100)/people
print("Each person should pay: " + round(calculations, 2))