print("Welcome to treasure Island")
print("Your mission is to find the traesure")
option1=input("you are at a cross of the road ,wher do you want to turn ? 'left' or 'right' ? \n")
if option1.lower() == "left":
    option2=input("You came to a lake.There is an island middle of the lake. Type 'wait' to wait for a boat.Type 'swim' to across ? \n" )
    if option2.lower() == "wait":
        option3=input("You are arrive at the island unharmed.Ther is a house with three doors. One red,one yellow and one blue. Which colour do you choose ?  \n")
        if option3.lower() == "blue":
            print("You choose door is wrong. Game over")
        elif option3.lower() == "red":
            print("You choose door is wrong. Game over")
        elif option3.lower() == "yellow":
            print("You choose door is correct. You find the treasure. You win.")
        else:
            print("You choose door that is doesn't exist. Game over")
    else:
        print("crocodile eat you. Game over")
else:
    print("road is closed. Game over")                
                
