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
