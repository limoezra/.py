import random
choices = ["rock", "paper", "scissors"]

computer = random.choices(choices)
player = None
while player not in choices:  
  player = input("rock,paper, or  scissors?:").lower()
if player == computer: 
  print ("computer: ",computer)
  print("player:" ,player)
  print("YOU LOSE!")