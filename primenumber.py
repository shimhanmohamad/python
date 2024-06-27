def is_prime(number):
    is_prime=True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

        print("It's not a prime number")

n = int(input("Enter a number you want to check if it is prime or not: "))
is_prime(number=n)
