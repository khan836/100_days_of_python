# print ("Welcome to the tip calculator!")
# total_bill = int(input("what was the total bill? $"))
# tip = int(input("how much tip would  you like to give? 10, 12 or 15? "))
# people = int(input("how many people to split the bill? "))
# tip_as_percent = tip / 100
# total_tip_amount = total_bill * tip_as_percent
# total_bill_with_tip = total_bill + total_tip_amount
# bill_per_person =total_bill_with_tip / people
# total_amouont = round(bill_per_person, 3)
# print(f"each person should pay : $ {total_amouont}")




# print("welcome to the tip calculator!")
# total_bill = int(input("what was the total bill? $ "))
# tip = int(input(" how much tip would you like to give ? 10, 12,or 15?"))
# people = int(input(" how many people to split the bill? "))
# tip_as_percent = tip / 100
# total_tip_amount = (total_bill) * tip_as_percent
# total_bill_with_tip = total_bill + total_tip_amount
# bill_per_person = total_bill_with_tip / people
# final_amount = round(bill_per_person, 2)
# print(f"each person should pay: ${final_amount}")



print("welcome to the tip calculator!")
total_bill = float(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give? 10,12 or 15?"))
people = int(input(" how many people to split the bill?"))
tip_as_percent = tip /100
tip_amount = total_bill * tip_as_percent
total_bill_with_tip = total_bill + tip_amount
bill_per_person = total_bill_with_tip / people
final_amount = round(bill_per_person, 2)
print(f"each person should pay: ${final_amount}")
