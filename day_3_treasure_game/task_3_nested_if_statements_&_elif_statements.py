print("welcome to the roller coaster!")
height = int(input("what is you rheight in cm?"))
if height > 120:
  print("you can ride")
  
  age = int(input("what is your age"))
  
  if age < 12:
    print("please pay $6")
  elif age <= 18:
    print("please pay $8")

  else:
    print("please pay $12")  

else:
  print("you cant ride daddy")  