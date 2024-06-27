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

mychoice = int(input("What do you choose ? Type 0 for rock, Type 1 for paper and Type 2 for scissor ? \n"))

if (0 <=mychoice or mychoice <= 2):
    if(mychoice == 0):
        print(rock)
    elif(mychoice == 1):
        print(paper)
    else:
        print(scissor)

    computer = random.randint(0,2)
    print("computer choose : \n")

    if(computer == 0):
        print(rock)
    elif(computer == 1):
        print(paper)
    else:
        print(scissor)


    if(mychoice == computer):
        print("Match draw")
    else:
        if(mychoice == 0  and computer == 2):
            print("You win")
        else:
            if(mychoice == 2  and computer == 1):
                print("You win")
            else:
                if(mychoice == 1  and computer == 0):
                    print("You win")
                else:
                    print("You lose")
else:
    print("Invalid input")

