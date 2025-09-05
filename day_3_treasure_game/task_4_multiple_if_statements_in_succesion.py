print("welcomr to the roller coaster!")
height = int(input("what is your height in cm?"))
bill = 0


if height > 120:
  print("you can ride")
  
  age = int(input("what is your age?"))
  
  if age < 12:
   bill = 5
   print("child tickets are $5")
  elif age <= 18 :
   bill = 7
   print("youth tickets are $7")
  else:
   bill = 12
   print("adults tickets are $12")

  photo = input("do you want a photo taken? y or n?")
  if photo == "y":
   bill +=3 

  print((f"your final bill is ${bill}")) 
  
              
else:
  print("Sorry, you're not tall enough to ride.")  