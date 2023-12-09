# UFCFT4-15-3 Cryptography Written Assessment
# Joe Holloway
# Student Number: 21016724

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

# ------------------------------ #
# Console interface

def run():
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
        run()

# ------------------------------ #
run()