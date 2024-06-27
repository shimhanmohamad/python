print("Welcome to the Python pizz deliveries")
size = input("What is the size of pizz do you want ? S,M or L ?")
add_pepperoni = input("Do you want pepperoni ? Y or N ?")
add_extarcheese = input("Do you want extra cheese ? Y or N ?")
# small_pizza = 15
# medium_pizza = 20
# large_pizza = 25
# pepperoni_for_smallpizza = 2
# pepperoni_for_medium_large = 3
# extarcheese_anypizza = 1
# bill = 0

# if size == "S":
#     if add_pepperoni == "Y":
#         if add_extarcheese == "y":
#             bill = bill + small_pizza + pepperoni_for_smallpizza + extarcheese_anypizza
#         else:
#             bill = bill + small_pizza + pepperoni_for_smallpizza
#     else:
#         if add_extarcheese == "Y":
#             bill = bill + small_pizza + extarcheese_anypizza
#         else:
#             bill = bill + small_pizza        

# elif size == "M":
#     if add_pepperoni == "Y":
#         if add_extarcheese =="Y":
#             bill = bill + medium_pizza + pepperoni_for_medium_large + extarcheese_anypizza
#         else:
#             bill = bill + medium_pizza + pepperoni_for_medium_large
#     else:
#         if add_extarcheese == "Y":
#             bill = bill + medium_pizza + extarcheese_anypizza
#         else:
#             bill = bill + medium_pizza

# else:
#     if add_pepperoni == "Y":
#         if add_extarcheese == "Y":
#             bill = bill + large_pizza + pepperoni_for_medium_large + extarcheese_anypizza
#         else:
#             bill = bill + large_pizza + pepperoni_for_medium_large
#     else:
#         if add_extarcheese == "Y":
#             bill = bill + large_pizza + extarcheese_anypizza
#         else:
#             bill = bill + large_pizza

# print(f"Your final bill : ${bill}.")
bill = 0
if size == "S":
    bill = bill +15
elif size == "M":
    bill = bill + 20
else:
    bill = bill + 25

if add_pepperoni == "Y":
    if size == "S":
        bill = bill + 2
    else:
        bill = bill + 3

if add_extarcheese == "Y":
    bill = bill + 1

print(f"Your final bill : $ {bill}")

      
