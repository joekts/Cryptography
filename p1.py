def validate_ISBN():
    # Print instructions
    print("Enter an ISBN to validate:")

    # Takes user input and sanitizes
    raw = input().replace("-", "")

    # Making sure input is 10 digits, otherwise restart process
    if len(raw) != 10:
        print("This is not an ISBN, try again")
        validate_ISBN()
        return

    # Initialize integer array
    ISBN = [0] * 10

    # Add user input to integer array
    for i in range(len(raw)):
        # Assigning digit to a temporary object
        temp = raw[i]

        # Checking for X in the ISBN and converting it to 10
        if temp == 'X':
            ISBN[i] = 10
        else:
            ISBN[i] = int(temp)

    # ISBN calculation and mod to validate ISBN
    count = 0

    for i in range(10):
        count += ISBN[i] * (i + 1)

    # Printing output depending on validation result
    if count % 11 == 0:
        print("Valid ISBN")
    else:
        print("Invalid ISBN")

def mini_ISBN():
    # Print instructions
    print("Enter a mini-ISBN to validate (digits only):")

    raw = input()

    # Restarts method if invalid number is given
    if len(raw) != 5 and len(raw) != 6:
        print("This is not a valid mini-ISBN, try again")
        mini_ISBN()
        return

    # Checking if 5 or 6 digits are given and using appropriate method
    if len(raw) == 6:
        # Initialize integer array
        ISBN = [0] * 6

        # Add user input to integer array
        for i in range(len(raw)):
            # Assigning digit to a temporary object
            temp = raw[i]

            # Checking for X in the ISBN and converting it to 10
            if temp == 'X':
                ISBN[i] = 10
            else:
                ISBN[i] = int(temp)

        # Calculating equation and reaching a total
        count = 0

        for i in range(len(raw)):
            count += ISBN[i] * (len(raw) - i)

        # Checking if total mod 7 = 0
        if count % 7 == 0:
            print("Valid mini-ISBN")
        else:
            print("Invalid mini-ISBN")
    else:
        # Initialize integer array
        ISBN = [0] * 5

        # Add user input to integer array
        for i in range(len(raw)):
            # Assigning digit to a temporary object
            temp = raw[i]

            # Checking for X in the ISBN and converting it to 10
            if temp == 'X':
                ISBN[i] = 10
            else:
                ISBN[i] = int(temp)

        count = 0

        for i in range(len(raw)):
            count += ISBN[i] * (6 - i)

        digit6 = []

        for i in range(11):
            if (count + i) % 7 == 0:
                digit6.append(i)

        if digit6:
            print("Possible outcomes for the sixth digit are: ")
            for i in digit6:
                print(i)
            print("The mini-ISBN number is " + raw + str(digit6))
        else:
            print("This does not seem to be a valid mini-ISBN")

# Call the functions to run the code
validate_ISBN()
mini_ISBN()
