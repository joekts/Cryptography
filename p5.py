import random

# PRNG
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

def random_operator():
    
    # Randomly chooses an operator
    operator = random.choice(['+', '-', '*', '/'])

    return operator

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def encryption(secret_msg, msg_no):

    # Generates a key
    key = generate_key(msg_no, len(secret_msg))

    # Convert secret message to hex string
    secret_msg = secret_msg.encode('utf-8').hex()

    # Convert key to hex string
    key = key.encode('utf-8').hex()

    # XOR the secret message and the key
    ciphertext = hex(int(secret_msg, 16) ^ int(key, 16))

    # Convert ciphertext to binary string
    ciphertext = bin(int(ciphertext, 16))

    # Separate the binary string into groups of 8
    ciphertext = [ciphertext[i:i+8] for i in range(2, len(ciphertext), 8)]

    # Convert the binary list into integers
    ciphertext = [int(i, 2) for i in ciphertext]

    return ciphertext

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

    print(positions)

    # Check if positions is empty
    if len(positions) != 0:
        
        # Calculate the number of groups
        groups = len(secret) // len(positions)


        # BROKEN NEEDS FIXING:
        # Loop through positions
        for i in range(len(positions)):
            addition = ''

            for i in range(groups):
                addition += str(secret.pop(0))

                if(i != groups - 1):
                    addition += random_operator()

            msg1[positions[i]] += addition

    # Convert list to string
    steg_msg = ' '.join(msg1)




    return steg_msg

#print(encryption("task17", 1))

#string = "How are you today? I had a very busy day! I travelled 400 miles returning to London. It was windy and rainy. The traffic was bad too. I managed to finish my job, ref No 3789. But I am really tired. If possible, can we cancel tonight’s meeting? See you soon. "
#print(string.split())

print(steganography("The meeting will take place at 514 St Andrew’s Place, at 2:30pm on Monday 12th December 2023. You should bring all necessary equipment with you, as none will be provided. Your bags may be searched on entry to the premises. Please do not be alarmed by this process, it is for your own safety and the safety of others. ", "task17", 1))