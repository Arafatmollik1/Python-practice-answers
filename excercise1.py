name = input("What is your name? ")
print("Hi, Nice to meet you", name)
    
number = int(input("Enter a random number between 1 to 100: "))

# Check if number is too big
if number > 100:
    print("Oops, you have input a wrong number")
else:
    # Check if number is even or odd
    # % (modulo) gives the remainder after division
    # If remainder of division by 2 is 0, number is even
    if number % 2 == 0:
        print("You have entered an even number")
    else:
        print("You have entered an odd number")
    