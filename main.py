import random

comp_num = random.randint(0,10)
tries = 3
won = False
play = True


while play == True:
  if won == True:
    print("Congrats, you won!")
    break
  while tries > 0:
    player_num = input("Enter a number between 1 and 10: ")
    player_num = float(player_num)
    if player_num < 0 or player_num > 10:
      print("Bad Number")
      break
    else:
      if player_num < comp_num:
        print("Number too small. Try again if you can")
        tries -= 1
        print("You have " + str(tries) + " tries left")
      elif player_num > comp_num:
        print("Number too big. Try again if you can")
        tries -= 1
        print("You have " + str(tries) + " tries left")
      else:
        print("Correct")
        won = True
        break
        if tries == 0:
          break


