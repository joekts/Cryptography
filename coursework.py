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
#mini_ISBN()

# ------------------------------ # # ------------------------------ # # ------------------------------ #
# Task 2: BCH Generating and Correcting
# ------------------------------ # # ------------------------------ # # ------------------------------ #

# ------------------------------ #
# Modulo 11 inverse and square root functions
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
# ------------------------------ #

# ------------------------------ #
# BCH Generator
def bch_encoder():
    # Print instructions
    print("Input 6 digits:")

    # Get user input
    raw = input()

    # Making sure the user has entered six digits, recursion if not
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

    # Printing the codeword
    print("Your codeword is:", end=" ")
    for digit in codeword:
        print(digit, end="")
    print()
# ------------------------------ #

# ------------------------------ #
# BCH Correcting
def bch_decoder():
    # Print instructions
    print("Enter a BCH(10,6) codeword:")

    # Get user input
    raw = input()

    # Check if user input is 10 digits
    if len(raw) != 10:
        print("Invalid BCH(10,6) codeword, try again")
        print()
        bch_decoder()
        return

    # Assign user input to an array
    codeword = [int(raw[i]) for i in range(10)]

    # Syndrome calculations
    s1 = sum(codeword) % 11
    s2 = sum((i + 1) * codeword[i] for i in range(10)) % 11
    s3 = sum((i + 1) * (i + 1) * codeword[i] for i in range(10)) % 11
    s4 = sum((i + 1) * (i + 1) * (i + 1) * codeword[i] for i in range(10)) % 11

    # Check if there are any errors
    if s1 == 0 and s2 == 0 and s3 == 0 and s4 == 0:
        print("No errors in this BCH(10,6) codeword")
    else:
        # PQR Calculations
        p = (s2 * s2 - s1 * s3) % 11
        q = (s1 * s4 - s2 * s3) % 11
        r = (s3 * s3 - s2 * s4) % 11

        # Check if there are 1 or 2 errors
        if p == 0 and q == 0 and r == 0:

            # Finding the position and magnitude of the error
            position = (s2 * inverse(s1)) % 11
            magnitude = s1

            # Correcting the error
            codeword[position - 1] = (codeword[position - 1] - magnitude) % 11

            # Printing the corrected codeword
            print(f"An error was found of magnitude {magnitude} in position {position} and has been corrected")
            print(f"The correct codeword is: {''.join(map(str, codeword))}")
        else:

            # Checking for 2 errors, or 3 or more errors
            if(sqrt( (q*q) - (4*p*r) ) == -1):

                print("There are 3 or more errors within this code")

            else:

                # Finding the position and magnitude of the errors
                i = ((-q + sqrt( (q*q) - (4*p*r) )) * inverse(2 * p)) % 11
                j = ((-q - sqrt( (q*q) - (4*p*r) )) * inverse(2 * p)) % 11

                b = (((i * s1) - s2) * inverse(i - j)) % 11
                a = (s1 - b) % 11

                # Correcting the errors
                codeword[i - 1] = (codeword[i - 1] - a) % 11
                codeword[j - 1] = (codeword[j - 1] - b) % 11

                # Printing the corrected codeword
                print("Two errors have been found and corrected in this codeword")
                print(f"Error in position {i} of magnitude {a}")
                print(f"Error in position {j} of magnitude {b}")
                print(f"The correct codeword is: {''.join(map(str, codeword))}")
# ------------------------------ #

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

# ------------------------------ # # ------------------------------ # # ------------------------------ #
# Task 4: A Text Encryption APP Using Stream Cipher and Steganography
# ------------------------------ # # ------------------------------ # # ------------------------------ #

# ------------------------------ #
# Importing libraries
import random
import re
# ------------------------------ #

# ------------------------------ #
# Pseudo Random Number Generator
def generate_key(msg_no, length):

    #Creates a one time pad for the message
    random.seed(msg_no)

    #Characters to choose from
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    #Creates a list of random numbers
    key = [random.randint(0, 61) for _ in range(length)]

    #Converts the random numbers to characters
    for i in range(len(key)):
        key[i] = characters[key[i]]

    # Creates string from list
    key = ''.join(key)

    return key
# ------------------------------ #

# ------------------------------ #
# Function to return one of the four operators randomly
def random_operator():
    
    # Randomly chooses an operator
    operator = random.choice(['+', '-', '*', '/'])

    return operator
# ------------------------------ #

# ------------------------------ #
# Function that checks if input string contains numbers/digits
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)
# ------------------------------ #

# ------------------------------ #
# Function that encrypts message 2 (secret message) using a one time pad
def encryption(secret_msg, msg_no):

    # Generates a key
    key = generate_key(msg_no, len(secret_msg))

    # Convert secret message to hex string
    secret_msg = secret_msg.encode('utf-8').hex()

    # Convert key to hex string
    key = key.encode('utf-8').hex()

    # XOR the secret message and the key
    ciphertext = hex(int(secret_msg, 16) ^ int(key, 16))

    # Convert ciphertext to binary string,
    ciphertext = bin(int(ciphertext, 16))
    
    # Separate the binary string into groups of 8
    ciphertext = [ciphertext[i:i+8] for i in range(2, len(ciphertext), 8)]

    # Convert the binary list into integers
    ciphertext = [int(i, 2) for i in ciphertext]

    return ciphertext
# ------------------------------ #

# ------------------------------ #
# Function that takes message 1 and message 2, uses the encryption function to encrypt message 2, and hides the encrypted message in message 1
def steganography(msg1, secret_msg, msg_no):

    # Encrypts the secret message
    secret = encryption(secret_msg, msg_no)

    # Split msg1
    msg1 = msg1.split()

    # Create a list to note positions of integers
    positions = []

    # Loop through msg1
    for i in range(len(msg1)):
        # If string is an integer
        if has_numbers(msg1[i]):
            # Add position to list
            positions.append(i)

    # If msg1 contains no digits, find all strings containing an 'e'
    if len(positions) == 0:

        # Loop through msg1 and find all the strings containing an 'e'
        for i in range(len(msg1)):
            if 'e' in msg1[i]:
                # Add position to list
                positions.append(i)

    # Loop through secret message and concatenate every two integers with a '.'
    for i in range(len(secret) // 2):
        secret[i] = str(secret[i]) + '.' + str(secret[i+1])
        secret.pop(i+1)


    # Check if positions is empty
    if len(positions) > 0:

        # Check if positions is longer than secret, means that can assign one integer to each position
        if len(positions) > len(secret):

            # Loop through positions
            for i in range(len(positions)):
                
                # Check if secret[i] exists
                if i < len(secret):

                    # Concatenates the secret message with the message
                    msg1[positions[i]] += ' [' + secret[i] + ']'

        # If positions is shorter than secret, means that need to assign more than one integer to each position
        else:

            # Calculate the group size, which is the number of integers to assign to each position
            group_size = (len(secret) // len(positions)) + 1

            # Loop through positions
            for i in range(len(positions)):

                if len(secret) > 0:
                    # Start the concatenation of the string with a '['
                    msg1[positions[i]] += ' ['

                # Loop through the group size
                for z in range(group_size):

                    # If down to the last integer, then concatenate with a ']' and break the loop
                    if len(secret) == 1:

                        msg1[positions[i]] += str(secret[0]) + ']'

                        # Remove the first element of the secret message
                        secret.pop(0)

                        break
                    
                    # Check if at the last integer of the group, then concatenate with a ']'
                    elif z == group_size - 1:

                        if len(secret) > 0:
                            msg1[positions[i]] += str(secret[0]) + ']'

                            # Remove the first element of the secret message
                            secret.pop(0)


                        
                    # Add integer with a random operator
                    elif len(secret) > 0:

                        # Concatenates the secret message with the message
                        msg1[positions[i]] += secret[0] + random_operator()

                        # Remove the first element of the secret message
                        secret.pop(0)
                    
    
    # Convert list to string
    msg1 = ' '.join(msg1)
    
    return msg1
# ------------------------------ #

# ------------------------------ #
# Function that takes the ciphertext and decrypts it, printing the original message 1 and message 2
def decryption(ciphertext, msg_no):

    # Split the ciphertext
    ciphertext = ciphertext.split()

    # Identify string surrounded by '[' and ']' and add to a list, remove them from the ciphertext
    secret = []
    for i in range(len(ciphertext)):
        if '[' in ciphertext[i]:
            secret.append(ciphertext[i])
            ciphertext[i] = ''

    # Strip the square brackets, then split the string by the operator and '.'
    for i in range(len(secret)):
        secret[i] = secret[i].strip('[]')
        secret[i] = re.split('\+|\-|\*|\/|\.', secret[i])

    # Convert the list of lists into a list of integers
    for i in range(len(secret)):
        for z in range(len(secret[i])):
            secret[i][z] = int(secret[i][z])

    # Assign the integers to a new list to remove list nesting
    secret2 = []
    for i in range(len(secret)):
        for z in range(len(secret[i])):
            secret2.append(secret[i][z])

    # Generate a key of length of the list
    key = generate_key(msg_no, len(secret2))

    # Convert the key into hexadecimal
    key = key.encode('utf-8').hex()

    # Convert the secret list of integers into binary removing the '0b' prefix
    secret2 = [bin(i)[2:] for i in secret2]

    # Adding leading zeros to all but the last binary string
    for i in range(len(secret2) - 1):
        secret2[i] = secret2[i].zfill(8)
    
    # Concatenate the binary strings
    secret2 = ''.join(secret2)

    # Convert the binary string into hexadecimal
    secret2 = hex(int(secret2, 2))

    # XOR the two hexadecimal strings
    secret2 = hex(int(secret2, 16) ^ int(key, 16))

    # Convert the hexadecimal string into a string
    secret2 = bytearray.fromhex(secret2[2:]).decode()

    # Join the ciphertext
    ciphertext = ' '.join(ciphertext)

    # Print the ciphertext and the secret message
    print('Ciphertext: ', ciphertext)
    print('Secret message: ', secret2)
# ------------------------------ #

# -------------------------
# Testing
# -------------------------

# ------------------------------ #
# Tests for the video demo as shown in Appendix 2
print('Test 1: ')
print('')
print('Encryption:')
print('')
print('Your encrypted message is: ', steganography('The meeting will take place at 514 St Andrew’s Place, at 2:30pm on Monday 12th December 2023. You should bring all necessary equipment with you, as none will be provided. Your bags may be searched on entry to the premises. Please do not be alarmed by this process, it is for your own safety and the safety of others.', 'task17', 1))
print('')
print('Decryption:')
print('')
decryption(steganography('The meeting will take place at 514 St Andrew’s Place, at 2:30pm on Monday 12th December 2023. You should bring all necessary equipment with you, as none will be provided. Your bags may be searched on entry to the premises. Please do not be alarmed by this process, it is for your own safety and the safety of others.', 'task17', 1), 1)
print('')
print('')
print('Test 2: ')
print('')
print('Encryption:')
print('')
print('Your encrypted message is: ', steganography('On arrival at the venue, you should ask at reception for Dr. Black. You will then be escorted to Dr. Black’s office on the 23rd floor, in room 713B. In case of difficulty, please telephone 01172 346852 for assistance.', 'Ask for Bob', 1))
print('')
print('Decryption:')
print('')
decryption(steganography('On arrival at the venue, you should ask at reception for Dr. Black. You will then be escorted to Dr. Black’s office on the 23rd floor, in room 713B. In case of difficulty, please telephone 01172 346852 for assistance.', 'Ask for Bob', 1), 1)
print('')
print('')
print('Test 3: ')
print('')
print('Encryption:')
print('')
print('Your encrypted message is: ', steganography('The threat has now been eradicated. All is well.', 'Beware threat still exists', 1))
print('')
print('Decryption:')
print('')
decryption(steganography('The threat has now been eradicated. All is well.', 'Beware threat still exists', 1), 1)
print('')
# ------------------------------ #

# ------------------------------ #
# Console application for effective use

print('Would you like to encrypt or decrypt a message? (e/d)')
choice = input()

print('')

if choice == 'e':
    print('Please enter your message:')
    msg = input()
    print('')
    print('Please enter your secret message:')
    secret = input()
    print('')
    print('Please enter the message number:')
    msg_no = input()
    print('')
    print('Your encrypted message is: ', steganography(msg, secret, msg_no))
    print('')
elif choice == 'd':
    print('Please enter your ciphertext:')
    ciphertext = input()
    print('')
    print('Please enter the message number:')
    msg_no = input()
    print('')
    decryption(ciphertext, msg_no)
    print('')
else:
    print('Invalid input')
# ------------------------------ #

