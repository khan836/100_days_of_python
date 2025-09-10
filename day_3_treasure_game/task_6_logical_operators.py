print(
  ''' 
_____________________                              _____________________
`-._:  .:'   `:::  .:\           |\__/|           /::  .:'   `:::  .:.-'
    \      :          \          |:   |          /         :       /    
     \     ::    .     `-_______/ ::   \_______-'   .      ::   . /      
      |  :   :: ::'  :   :: ::'  :   :: ::'      :: ::'  :   :: :|       
      |     ;::         ;::         ;::         ;::         ;::  |       
      |  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:::  .:'   `:|       
      /     :           :           :           :           :    \       
     /______::_____     ::    .     ::    .     ::   _____._::____\      
                   `----._:: ::'  :   :: ::'  _.----'                    
                          `--.       ;::  .--'                           
                              `-. .:'  .-'                               
                                 \    / :F_P:                            
                                  \  /                                   
                                   \/  ''')
print("welcome to the treasure island>")
print("you mission is to find the treasure")
choice_1 = input("you are at a cross road, where do you want to go? type 'Left or 'Right'\n").upper()
if choice_1 == "left":
  choice_2 = input("now you\" have come to a lake. you wanna wait or swim? type 'wait' to wait or 'swim' to swim\n").upper()
  if choice_2 == "wait":
    choice_3 = input("choose a door: red; blue or yellow\n").upper()
    if choice_3 == "yellow":
      print("you found the treasure you win")
    elif choice_3 == "red":
      print("you gor burned by fire. game over")
    elif choice_3 == "blue":
      print("you got eaten by beasts.game over")    
  else:
    print("you got attacked by a fish. game over")  

else:
  print("you fell into a hole. game over")  