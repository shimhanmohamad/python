print("Welcome to Love calculater")
myname = input("What is your name ? ")
othername = input("What is your lover name ? ")
lowercase_myname = myname.lower()
lowercase_othername = othername.lower()

combined_name = myname + othername
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true = t + r + u +e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

if love_score < str(10)  or  love_score > str(90):
    print(f"your love score is {love_score},you go together like cock and mentos.") 
elif love_score > str(40) and love_score < str(50):
    print(f"your love score is {love_score},you are alright together.")
else:
    print(f"your love score is {love_score}.")


# total1 = 0
# total2 = 0
# total3 = 0
# total4 = 0
# if lowercase_myname.count("t") > 0 or lowercase_myname.count("r") > 0 or lowercase_myname.count("u") > 0 or lowercase_myname.count("e") > 0:
#     total1 = total1 + int(lowercase_myname.count("t") + lowercase_myname.count("r") + lowercase_myname.count("u") + lowercase_myname.count("e"))

# if lowercase_myname.count("l") > 0 or lowercase_myname.count("o") > 0 or lowercase_myname.count("v") > 0 or lowercase_myname.count("e") > 0:
#     total2 = total2 + int(lowercase_myname.count("l") + lowercase_myname.count("o") + lowercase_myname.count("v") + lowercase_myname.count("e"))

# total3 = 0
# total4 = 0

# if lowercase_othername.count("t") > 0 or lowercase_othername.count("r") > 0 or lowercase_othername.count("u") > 0 or lowercase_othername.count("e") > 0:
#     total3 = total3 + int(lowercase_othername.count("t") + lowercase_othername.count("r") + lowercase_othername.count("u") + lowercase_othername.count("e"))

# if lowercase_othername.count("l") > 0 or lowercase_othername.count("o") > 0 or lowercase_othername.count("v") or lowercase_othername.count("e")> 0:
#     total4 = total4 + int(lowercase_othername.count("l") + lowercase_othername.count("o") + lowercase_othername.count("v")+lowercase_othername.count("e"))

# total_t = total1 + total3
# total_l = total2 + total4

# percentage = str(total_t) + str(total_l)
#print(f"your love percentage is {percentage}%")

# if percentage < str(10)  or  percentage > str(90):
#     print(f"your love score is {percentage},you go together like cock and mentos.") 
# elif percentage > str(40) and percentage < str(50):
#     print(f"your love score is {percentage},you are alright together.")
# else:
#     print(f"your love score is {percentage}.")    
   