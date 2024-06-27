import random
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/''')
HANGMANPICS = [ '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']
word = [
    "lion", "tiger", "elephant", "giraffe", "cheetah", "zebra", "koala", "kangaroo", "platypus", "penguin", 
    "dolphin", "whale", "shark", "octopus", "seagull", "parrot", "gorilla", "monkey", "chimpanzee", "lemur", 
    "panda", "koala", "sloth", "armadillo", "hedgehog", "rhinoceros", "hippopotamus", "crocodile", "alligator", 
    "snake", "lizard", "turtle", "frog", "toad", "newt", "salamander", "iguana", "komodo dragon", "beaver", 
    "otter", "seal", "walrus", "polar bear", "grizzly bear", "black bear", "panda bear", "koala bear", "brown bear", 
    "penguin", "ostrich", "eagle", "hawk", "owl", "bat", "fox", "wolf", "coyote", "jackal", "hyena", 
    "moose", "deer", "elk", "reindeer", "antelope", "gazelle", "giraffe", "camel", "llama", "alpaca", 
    "horse", "zebra", "donkey", "mule", "goat", "sheep", "cow", "pig", "boar", "deer", 
    "rabbit", "hare", "squirrel", "chipmunk", "rat", "mouse", "beaver", "otter", "skunk", "badger", 
    "raccoon", "opossum", "koala", "kangaroo", "wallaby", "wombat", "numbat", "quokka", "bandicoot", "tasmanian devil"
]

chooseaword = random.choice(word)
print(f"print the choosen word : {chooseaword}")
blanks = []

for i in range(len(chooseaword)):
    blanks += "_"
print(blanks)

lives = 6

end_of_game = False
while  not end_of_game:
    guess = input("Guess a letter  : ") 
    
    if guess in blanks:
        print(f"You already guessed {guess}")   
    if guess not in chooseaword:
       print(f"You gussed letter {guess}  not in the word, You lose a life")
       lives-=1
       if lives == 0:
            end_of_game=True
            print("You lose")
    
    for position  in range(len(chooseaword)):
        if chooseaword[position] == guess:
            blanks[position] = chooseaword[position]
    
    print(blanks)
    if "_" not in blanks:
        end_of_game = True
        print("You win")
    
    print(HANGMANPICS[lives])
         



