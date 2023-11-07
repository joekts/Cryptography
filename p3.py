def bch_decoder():
    print("Enter a BCH(10,6) codeword:")
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

    if s1 == 0 and s2 == 0 and s3 == 0 and s4 == 0:
        print("No errors in this BCH(10,6) codeword")
    else:
        # PQR Calculations
        p = (s2 * s2 - s1 * s3) % 11
        q = (s1 * s4 - s2 * s3) % 11
        r = (s3 * s3 - s2 * s4) % 11

        if p == 0 and q == 0 and r == 0:
            position = (s2 * inverse(s1)) % 11
            magnitude = s1

            codeword[position - 1] = (codeword[position - 1] - magnitude) % 11

            print(f"An error was found of magnitude {magnitude} in position {position} and has been corrected")
            print(f"The correct codeword is: {''.join(map(str, codeword))}")
        else:

            if(sqrt( (q*q) - (4*p*r) ) == -1):
                print("There are 3 or more errors within this code")
            else:
                i = ((-q + sqrt( (q*q) - (4*p*r) )) * inverse(2 * p)) % 11
                j = ((-q - sqrt( (q*q) - (4*p*r) )) * inverse(2 * p)) % 11

                b = (((i * s1) - s2) * inverse(i - j)) % 11
                a = (s1 - b) % 11

                codeword[i - 1] = (codeword[i - 1] - a) % 11
                codeword[j - 1] = (codeword[j - 1] - b) % 11

                print("Two errors have been found and corrected in this codeword")
                print(f"Error in position {i} of magnitude {a}")
                print(f"Error in position {j} of magnitude {b}")
                print(f"The correct codeword is: {''.join(map(str, codeword))}")

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

# Call the bch_decoder function to run the code
bch_decoder()
