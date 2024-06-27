import random
test_seed = int(input("Create a seed number : "))
random.seed(test_seed)

head_tail = random.randint(0,1)
if head_tail == 1:
    print("Head")
else:
    print("Tail")