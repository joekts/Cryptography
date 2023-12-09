# UFCFT4-15-3 Cryptography Written Assessment
# Joe Holloway
# Student Number: 21016724

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

# Code runs in console, no parameters or return values
#bch_encoder()
#bch_decoder()