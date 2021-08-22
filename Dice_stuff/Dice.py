# sourcery skip: for-index-underscore, simplify-numeric-comparison
import random
 
Playeronewin = 0
Playertwowin = 0
 
number = 0
 
number2 = 0
 
 
while True:
 password = input("enter your password player 1, ")
 if password == "CUBE":
    print ("welcome to my game")
    break
 else:
    print ("you are locked out")
#this is where you put in the password to get into the game
 
 
while True:
 password2 = input("enter your password player 2, ")
 if password2 == "CUBE2":
    print ("welcome to my game")
    break
 else:
    print ("you are locked out")
 
 
#this is where you save the names and they are saved to a file
 
name1 = input("what is your name player 1, ")
 
name2 = input("what is your name player 2, ")
 
#this is the part where the dice is rolled for player one
for score in range(5):
  print ("This is a dice rolling progarm")
  for i in range(1):
    player1 = input("press enter to roll player 1")
  number = random.randint(1,6)
 
 
  if number==1:
       print ("[———----]")
       print ("[       ]")
       print ("[   0   ]")
       print ("[       ]")
       print ("[———----]")
 
 
 
  if number==2:
       print ("[———----]")
       print ("[   0   ]")
       print ("[       ]")
       print ("[   0   ]")
       print ("[———----]")
 
 
  if number==3:
       print ("[———----]")
       print ("[     0 ]")
       print ("[   0   ]")
       print ("[ 0     ]")
       print ("[———----]")
 
 
  if number==4:
       print ("[———----]")
       print ("[ 0   0 ]")
       print ("[       ]")
       print ("[ 0   0 ]")
       print ("[———----]")
 
  if number==5:
       print ("[———----]")
       print ("[ 0   0 ]")
       print ("[   0   ]")
       print ("[ 0   0 ]")
       print ("[———----]")
 
 
  if number==6:
       print ("[———----]")
       print ("[ 0 0 0 ]")
       print ("[       ]")
       print ("[ 0 0 0 ]")
       print ("[———----]")
 
  print("Player 1 rolled", number)
 
  for i in range(1):
    player2 = input("press enter to roll Player 2")
  number2 = random.randint(1,6)
#this is the part where the dice is rolled for player two
 
  if number2==1:
       print ("[———----]")
       print ("[       ]")
       print ("[   0   ]")
       print ("[       ]")
       print ("[———----]")
 
 
 
  if number2==2:
       print ("[———----]")
       print ("[   0   ]")
       print ("[       ]")
       print ("[   0   ]")
       print ("[———----]")
 
 
  if number2==3:
       print ("[———----]")
       print ("[     0 ]")
       print ("[   0   ]")
       print ("[ 0     ]")
       print ("[———----]")
 
 
  if number2==4:
       print ("[———----]")
       print ("[ 0   0 ]")
       print ("[       ]")
       print ("[ 0   0 ]")
       print ("[———----]")
 
  if number2==5:
       print ("[———----]")
       print ("[ 0   0 ]")
       print ("[   0   ]")
       print ("[ 0   0 ]")
       print ("[———----]")
 
 
  if number2==6:
       print ("[———----]")
       print ("[ 0 0 0 ]")
       print ("[       ]")
       print ("[ 0 0 0 ]")
       print ("[———----]")
 
  print("Player 2 rolled", number2)
 
  print("'''''''''''''''''''''''")
  print("''''''''RESULTS''''''''")
  print("'''''''''''''''''''''''")
 
 
 
  print("End of Round 1")
 
  print(name1,"Has rolled",number)
 
  print(name2,"Has rolled",number2)

 
if number > number2:
      print (name1, "has won round 1")
elif number == number2:
      print ("round 1 is a tie")
else:
      print(name2, "has won round 1")
 
 
print("'''''''''''''''''''''''''''''")
print("''''''''ROUND 1 PART2''''''''")
print("'''''''''''''''''''''''''''''")
for i in range(1):
  player1 = input("press enter to roll player 1")
number3 = random.randint(1,6)
 
 
if number3==1:
       print ("[———----]")
       print ("[       ]")
       print ("[   0   ]")
       print ("[       ]")
       print ("[———----]")
 
 
 
if number3==2:
       print ("[———----]")
       print ("[   0   ]")
       print ("[       ]")
       print ("[   0   ]")
       print ("[———----]")
 
 
if number3==3:
       print ("[———----]")
       print ("[     0 ]")
       print ("[   0   ]")
       print ("[ 0     ]")
       print ("[———----]")
 
 
if number3==4:
       print ("[———----]")
       print ("[ 0   0 ]")
       print ("[       ]")
       print ("[ 0   0 ]")
       print ("[———----]")
 
if number3==5:
       print ("[———----]")
       print ("[ 0   0 ]")
       print ("[   0   ]")
       print ("[ 0   0 ]")
       print ("[———----]")
 
 
if number3==6:
       print ("[———----]")
       print ("[ 0 0 0 ]")
       print ("[       ]")
       print ("[ 0 0 0 ]")
       print ("[———----]")
 
print("Player 1 rolled", number)
 
for i in range(1):
  player2 = input("press enter to roll Player 2")
number4 = random.randint(1,6)
#this is the part where the dice is rolled for player two
 
if number4==1:
       print ("[———----]")
       print ("[       ]")
       print ("[   0   ]")
       print ("[       ]")
       print ("[———----]")
 
 
 
if number4==2:
       print ("[———----]")
       print ("[   0   ]")
       print ("[       ]")
       print ("[   0   ]")
       print ("[———----]")
 
 
if number4==3:
       print ("[———----]")
       print ("[     0 ]")
       print ("[   0   ]")
       print ("[ 0     ]")
       print ("[———----]")
 
 
if number4==4:
       print ("[———----]")
       print ("[ 0   0 ]")
       print ("[       ]")
       print ("[ 0   0 ]")
       print ("[———----]")
 
if number4==5:
       print ("[———----]")
       print ("[ 0   0 ]")
       print ("[   0   ]")
       print ("[ 0   0 ]")
       print ("[———----]")
 
 
if number4==6:
       print ("[———----]")
       print ("[ 0 0 0 ]")
       print ("[       ]")
       print ("[ 0 0 0 ]")
       print ("[———----]")
 
print("Player 2 rolled", number4)
 
print("'''''''''''''''''''''''")
print("''''''''RESULTS''''''''")
print("'''''''''''''''''''''''")
 
print("End of Round 1")
 
if (number + number3 % 2) == 0:
  print(name1,"{0} is Even".format(number + number3 + 10))
else:
  print(name1,"{0} is Odd".format(number + number3 - 5))

if (number2 + number4 % 2) == 0:
  print(name2,"{0} is Even".format(number2 + number4 + 10))
else:
  print(name2,"{0} is Odd".format(number2 + number4 - 5))

if number + number3 - 5 < 1: 
  print("This is invalid")

if number2 + number4 - 5 < 1: 
  print("This is invalid")

if number + number3 > number2 + number4:
      print (name1, "has won round 1")
elif number + number3 == number2 + number4:
      print ("round 1 is a tie")
else:
      print(name2, "has won round 1")






