print("Welcome to leap year finder!!!")
year=int(input("Enter the year do you want check if it is leap or not : "))
if year %  4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")        