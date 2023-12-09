# UFCFT4-15-3 Cryptography Written Assessment
# Joe Holloway
# Student Number: 21016724

# ------------------------------ # # ------------------------------ # # ------------------------------ #
# Task 1: Mini-ISBN
# ------------------------------ # # ------------------------------ # # ------------------------------ #

def mini_ISBN():
    # Print instructions
    print("Enter a mini-ISBN to validate (digits only):")

    # User input
    raw = input()

    # Restarts method through recursion if invalid number is given
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

            # Checking for X in the ISBN and converting it to 10
            if raw[i] == 'X':
                ISBN[i] = 10
            else:
                ISBN[i] = int(raw[i])

        # Initialising count variable
        count = 0

        # Calculating equation and reaching a total
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

            # Checking for X in the ISBN and converting it to 10
            if raw[i] == 'X':
                ISBN[i] = 10
            else:
                ISBN[i] = int(raw[i])

        # Initialising count variable
        count = 0

        # Calculating equation and reaching a total
        for i in range(len(raw)):
            count += ISBN[i] * (6 - i)

        # Initialising array for possible outcomes
        digit6 = []

        #  Adding valid digits to the array
        for i in range(11):
            if (count + i) % 7 == 0:
                digit6.append(i)

        # Printing possible outcomes
        if digit6:
            print("Possible outcomes for the sixth digit are: ")
            for i in digit6:
                print(i)
            print("The mini-ISBN number is " + raw + str(digit6))
        else:
            print("This does not seem to be a valid mini-ISBN")

# No parameters or return values, method operates within console
mini_ISBN()