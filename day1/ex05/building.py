import sys


def main():
    """
        caca
    """
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    myInput = ""
    if len(sys.argv) < 2:
        try :
            myInput = input("What is the text to count?\n")
        except EOFError:
            print("Input interrupted. Exiting...")
            return
    else :
        myInput = sys.argv[1]
    upperCase = 0
    lowerCase = 0
    digits = 0
    punctuation = 0
    space = 0
    for i in range(len(myInput)):
        if (myInput[i].isdigit()):
            digits += 1
        elif (myInput[i].islower()):
            lowerCase += 1
        elif (myInput[i].isupper()):
            upperCase += 1
        elif (myInput[i].isspace()):
            space += 1
        else:
            punctuation += 1
    print(f"The text contains {space + digits + lowerCase + upperCase + punctuation} characters:")
    print(f"{upperCase} upper letters")
    print(f"{lowerCase} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digits} digits")
    return


if __name__ == "__main__":
    main()
