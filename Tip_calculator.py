
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

#tip_amount = total_bill * (tip_percentage / 100)

#total_amount = total_bill + tip_amount
total_amount = total_bill * (1 + tip_percentage / 100)

#ind_payment = round(total_amount / people, 2)
ind_payment = total_amount / people

#print(f"Each person should pay: ${ind_payment}")
print(f"Each person should pay: ${ind_payment:.2f}")