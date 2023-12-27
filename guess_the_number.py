#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import os
import random

again='y'

while again=='y':
  from art import logo
  print(logo)
  is_game_over=False
  key_num=random.randint(1, 100)
  mode=input("Select gamemode: type 'e' for easy or 'h' for hard")
  
  while mode.lower()!='e' and mode.lower()!='h':
    mode=input("Select gamemode: type 'e' for easy or 'h' for hard")
  if mode.lower()=='e':
    tries=10
  elif mode.lower()=='h':
    tries=5
  
  print("I'm thinking of a number between 1 and 100.")
  while is_game_over==False:
    while tries>0:
      print(f"You have {tries} attempts remaining to guess the number.")
      guess=int(input("Make a guess:"))
      while guess<1 or guess>100:
        guess=int(input("Make a guess:"))
      if key_num<guess:
        print("Too high.")
      elif key_num>guess:
        print("Too low.")
      elif key_num==guess:
        print(f"You got it! The answer was {key_num}")
        is_game_over=True
        break
      tries-=1
    if tries==0:
      print("You ran out of attempts.")
      print(f"The correct number was {key_num}.")
      is_game_over=True
  
  again=input("Do you want to play again? Type 'y' or 'n'")
  while again.lower()!='y' and again.lower() != 'n':
    again=input("Do you want to play again? Type 'y' or 'n'")
  if again=='y':
    os.system('clear')
