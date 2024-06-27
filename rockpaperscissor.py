import random

# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("welcome to rock paper scissor Game!!!")
mychoice = int(input("What do you choose ? Type 0 for Rock, 1 for paper or 2 for  Scissor.? \n"))
if 0 <= mychoice <= 2:
    if mychoice == 0:
        print(rock)
    elif mychoice == 1:
        print(paper)
    else:
        print(scissor)

    computer_choice = random.randint(0,2)

    if computer_choice == 0:
        print(f"computer choice : \n {rock}")
    elif computer_choice == 1:
        print(f"computer choice : \n {paper}")
    else:
        print(f"computer choice : \n {scissor}")


    if mychoice == computer_choice:
        print("Match Draw")
    else:
        if (mychoice == 0 and computer_choice == 2):
            print("you win")
        else:
            if(mychoice == 2 and computer_choice == 1):
                print("you win")
            else:
                if(mychoice == 1 and computer_choice == 0):
                    print("you win")
                else:
                    print("you lose")
                
else:
    print("Invalid input ,You lose")                
    




