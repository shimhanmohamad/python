import random
word = ["ardvark","baboon","camel"]
chooseaword = random.choice(word)
# print(chooseaword)
guess = input("Guess a letter : ").lower()
for i in range(len(chooseaword)):
    if guess == chooseaword[i]:
        print("right")
    else:
        print("Wrong")
