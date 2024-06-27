print("Create your account")
userName = input("Input User name : ")
Password = input("Input password : ")
print("user "+userName+" created successfully")
print("Login Now")
user = input("Input User name : ")
if(user == userName):
    passw = input("Input password : ")
    if(passw == Password):
        print("User looged sucessfully")
    else:
        print("Invalid credential")
else:
    print("Invalid credential")