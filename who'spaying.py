import random
test_seed = int(input("Create a seed numbber : "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names,seperated by comma : ")
names = namesAsCSV.split(",")

print(names)

random_bill = random.randint(0,len(names)-1)
print(names[random_bill]+" is going to pay bill")
