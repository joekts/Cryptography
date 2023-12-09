# UFCFT4-15-3 Cryptography Written Assessment
# Joe Holloway
# Student Number: 21016724

# ------------------------------ # # ------------------------------ # # ------------------------------ #
# Task 3: Brute Force Password Cracking
# ------------------------------ # # ------------------------------ # # ------------------------------ #

# ------------------------------ #
# Imported Libraries
import hashlib
import itertools
import time
# ------------------------------ #


# ------------------------------ #
# Altered functions from Task 1 and 2 to be used in Task 3
def mini_ISBN(raw):
    
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
        return True
    else:
        return False
    
def bch_encoder(raw):

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
        return False

    # Concatenating the codeword
    codeword = ''.join(str(i) for i in codeword)

    return codeword
# ------------------------------ #

# ------------------------------ #
#Function to hash an input string and return hexadecimal digest
def hash_string(string):
    return hashlib.sha1(string.encode('utf-8')).hexdigest()
# ------------------------------ #

# ------------------------------ #
# Function to brute force a hashed password
def brute_force():
    # Choose a set instructions
    print("Choose a set to brute force (A, B or C):")

    # Get user input
    set = input()

    # Check if input is valid, if not restart function
    if set != 'A' and set != 'B' and set != 'C':
        print("Invalid set, try again")
        brute_force()
        return
    
    # Print instructions
    print("Enter a hashed password to brute force:")

    # Get user input
    hashed_password = input()
    
    # Start timer
    start = time.time()

    # Initialize variables
    cracked_password = ''
    max_length = 6
    
    if set == 'A':

        # Define characters to use in brute force
        characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

        # Loop through all possible codeword lengths
        for length in range(1, max_length + 1):
            # Generate and loop through all possible combinations of characters
            for guess in itertools.product(characters, repeat=length):

                # Convert guess to string
                guess = ''.join(guess)

                #Check if hash of guess matches hashed_password, and break loop if it does
                if hash_string(guess) == hashed_password:
                    cracked_password = guess
                    break
            
            # Break out of outer loop if password is cracked
            if cracked_password != '':
                break
    
    elif set == 'B':

        # Define characters to use in brute force
        characters = '0123456789X'

        # Generate and loop through all possible combinations of characters
        for guess in itertools.product(characters, repeat =6):

            # Convert guess to string
            guess = ''.join(guess)

            #Check if hash of guess matches hashed_password, and break loop if it does
            if mini_ISBN(guess):
                if hash_string(guess) == hashed_password:
                    cracked_password = guess
                    break

            

    elif set == 'C':
            
        # Define characters to use in brute force
        characters = '0123456789'

        # Generate and loop through all possible combinations of characters
        for guess in itertools.product(characters, repeat=6):
            # Convert guess to string
            guess = ''.join(guess)

            # Encode guess using BCH encoder
            guess = bch_encoder(guess)

            # Check if guess is a valid BCH codeword
            if guess != False:
                #Check if hash of guess matches hashed_password, and break loop if it does
                if hash_string(guess) == hashed_password:
                    cracked_password = guess
                    break

    # Stop timer
    end = time.time()

    # Print results
    
    print("Password:", cracked_password)
    print("Time taken:", end - start, "seconds")
# ------------------------------ #

# Code runs in console, no parameters or return values
brute_force()