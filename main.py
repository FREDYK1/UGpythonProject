while True:
    try:
        number = int(input("Enter your number: "))
        if (number % 3) == 0 and number != 0:
            print("Fizz")
        elif (number % 5) == 0 and number != 0:
            print("Buzz")
        elif (number % 3) == 0 and (number % 5) == 0 and number != 0:
            print("FizzBuzz")
        elif number == 0:
            break
        else:
            print("The number is not divisible by 3 and 5")
    except ValueError:
        print("Words aren't accepted. Please Enter a number.")
        continue
print("Zero is divisible by every number and ends the program")