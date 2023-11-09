import hashlib
import itertools
import time

#Function to hash an input string and return hexdecimal digest
def hash_string(string):
    return hashlib.sha1(string.encode('utf-8')).hexdigest()

# Set A
def brute_force():
    # Print instructions
    print("Enter a hashed password to brute force:")

    # Get user input
    hashed_password = input()

    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    cracked_password = ''
    max_length = 6

    # Start timer
    start = time.time()

    # Loop through all possible combinations of characters
    for length in range(1, max_length + 1):
        # Generate and loop through all possible combinations of characters
        for guess in itertools.product(characters, repeat=length):
            # Convert guess to string
            guess = ''.join(guess)
            print(guess)
            #Check if hash of guess matches hashed_password
            if hash_string(guess) == hashed_password:
                cracked_password = guess
                break

    # Stop timer
    end = time.time()

    # Print results
    if cracked_password:
        print("Password cracked:", cracked_password)
    else:
        print("Password could not be cracked")

    print("Time taken:", end - start, "seconds")

brute_force()

#Methods from previous practicals for Set B and C

def mini_ISBN(raw):
    # Print instructions
    print("Enter a mini-ISBN to validate (digits only):")

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

def bch_encoder():
    print("Input 6 digits:")
    raw = input()

    # Making sure the user has entered six digits
    if len(raw) != 6:
        print("Unusable number, try again")
        print()
        bch_encoder()
        return

    # Creating an array
    codeword = [0] * 10

    # Adding user input into the array
    for i in range(len(raw)):
        codeword[i] = int(raw[i])

    # Calculations for parity digits
    codeword[6] = (4 * codeword[0] + 10 * codeword[1] + 9 * codeword[2] + 2 * codeword[3] + 1 * codeword[4] + 7 * codeword[5]) % 11
    codeword[7] = (7 * codeword[0] + 8 * codeword[1] + 7 * codeword[2] + 1 * codeword[3] + 9 * codeword[4] + 6 * codeword[5]) % 11
    codeword[8] = (9 * codeword[0] + 1 * codeword[1] + 7 * codeword[2] + 8 * codeword[3] + 7 * codeword[4] + 7 * codeword[5]) % 11
    codeword[9] = (1 * codeword[0] + 2 * codeword[1] + 9 * codeword[2] + 10 * codeword[3] + 4 * codeword[4] + 1 * codeword[5]) % 11

    # Ensuring no parity digits are 10
    if 10 in codeword[6:]:
        print("Unusable number, try again")
        print()
        bch_encoder()
        return

    print("Your codeword is:", end=" ")
    for digit in codeword:
        print(digit, end="")
    print()

def mod11(integer):
    return integer % 11

def inverse(integer):
    for i in range(1, 11):
        if (integer % 11) * (i % 11) % 11 == 1:
            return i
    return 1

def sqrt(integer):
    integer = integer % 11
    if integer == 1:
        return 1
    elif integer == 3:
        return 5
    elif integer == 4:
        return 2
    elif integer == 5:
        return 4
    elif integer == 9:
        return 3
    else:
        return -1
    
