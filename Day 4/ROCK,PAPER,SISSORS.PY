import random
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
Scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images= [rock, Paper,Scissors]

mychoise=int(input("for rock enter 0, for paper enter 1, for sissors enter 2"))
print(game_images[mychoise])

computer_choise=random.randint(a=0,b=2)
print(game_images[computer_choise])
print(f"computer choise {computer_choise}")
if mychoise==0 and computer_choise== 2:
    print("You Win!")
elif computer_choise==0 and mychoise==2:
    print("computer wins!")
elif computer_choise > mychoise:
    print("Computer Wins!")
elif mychoise > computer_choise:
    print("you win!")
elif computer_choise==mychoise:
    print("its a draw")
else:
    print("not a vallid move")
