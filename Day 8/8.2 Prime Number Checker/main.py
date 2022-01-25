# Write your code below this line 👇
def prime_checker(number):
    # define a flag variable
    flag = False

    # prime numbers are greater than 1
    if number > 1:
        # check for factors
        for i in range(2, number):
            if (number % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag:
        print(number, "is not a prime number.")
    else:
        print(number, "is a prime number.")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)