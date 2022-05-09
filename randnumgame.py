## need a range
#input program: num from user 
#program defined (firstNum, secondNum)
#Output: clue, score

import random

 
def guess():
  x = 1
  y = 10
  ans = random.randint(1,10)
  score = 100
  
  clue =""
  while True:
    Userint= int(input("enter a number: "))
    if Userint > ans:
      clue = ("guess smaller")
    if Userint < ans:
      clue = ("guess bigger")
    if Userint== ans:
      return print ("good")
    
    print (clue)
   
guess ()