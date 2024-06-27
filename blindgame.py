logo = '''
    ⠀⠀⣀⣤⣶⣾⣿⣿⣿⣷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠋⣉⣀⣤⣴⠾⢛⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡈⠛⠛⢛⣉⣉⠁⠠⢤⣶⣶⣿⣿⣿⣯⣽⣶⣾⣛⡃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⡆⠘⠛⠛⠃⢰⣶⣦⠙⠛⠛⠛⠛⠉⠉⣉⣉⡉⠁⠀⠀
⠀⠀⠀⠀⠀⢀⡄⢀⡀⠀⢺⣿⣿⣇⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀
⠀⠀⠀⠀⢀⡾⠁⣼⡇⠀⠀⢹⣿⣿⣷⣄⠙⣻⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠀⠀
⠀⠀⠀⢀⣾⠃⣸⣿⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠃⠀⠀⠀
⠀⠀⣠⣾⠃⣸⣿⣿⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀
⠀⠀⠻⠏⢰⣿⣿⣿⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠉⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⠿⠟⠛⠛⠀⠀⠀⠀⠀⠉⠛⠿⠿⣿⠇⠀⠀
'''

# print(logo)
# print("Welcom to secrate auction game")
# name = input("Enter your name : ")
# amount = input("Entr your bid amount :$ ")
# option = input("Are there any bidder ? Type 'yes' or 'no'? ")
# bid_game = {}
# while option.lower() != "no":
#     name = input("Enter your name : ")
#     amount = input("Entr your bid amount :$ ")
#     option = input("Are there any bidder ? Type 'yes' or 'no'? ")

#     bid = {}
#     bid["name"] = name
#     bid["amount"] = amount
#     bid_game.append(bid)
#     bid_game.clear()

# print(bid)

bids ={}
bidding_finished = False

while not bidding_finished:
    nmae = input("What is yur name : ")
    price = input("what is your bid : ")
    bids[name] = price
    shoul_continue = input("Are there any bidders ? type 'yes' or 'no'")
    if shoul_continue == "no":
        bidding_finished = True
    elif shoul_continue == "yes":
        clear()