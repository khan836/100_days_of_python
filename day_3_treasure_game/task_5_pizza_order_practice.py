print("welcome to python pizza deliveries!")
size = input("what size pizza do you want? S, M or L?")
pepperoni = input("do you want pepperonu on your pizza? Y or N?")
extra_cheese = input("do you want extra cheese? Y or N?")
bill = 0

# todo: work out how much they need to pay based on their size choice?

if size == "s":
  bill += 15
elif size == "m":
  bill += 20
elif size == "l":
  bill += 25
else:
  print("you have not selected a valid size")       

# todo : work out how mucbh to add to their bill based on their pepperoni choice?
if pepperoni == "y":
  if size == "s":
    bill += 2
  else:
    bill +=3  

# todo: work out their final amount based on whether if they want extra cheese or not?
if extra_cheese == "y":
  bill+= 1

print(f"your final bill is ${bill}")  