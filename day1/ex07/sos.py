import sys

NESTED_MORSE = {" ": "/",
                "A": ".-",
                "B": "-...",
                "C": "-.-.",
                "D": "-..",
                "E": ".",
                "F": "..-.",
                "G": "--.",
                "H": "....",
                "I": "..",
                "J": ".---",
                "K": "-.-",
                "L": ".-..",
                "M": "--",
                "N": "-.",
                "O": "---",
                "P": ".--.",
                "Q": "--.-",
                "R": ".-.",
                "S": "...",
                "T": "-",
                "U": "..-",
                "V": "...-",
                "W": ".--",
                "X": "-..-",
                "Y": "-.--",
                "Z": "--..",
                "0": "-----",
                "1": ".----",
                "2": "..---",
                "3": "...--",
                "4": "....-",
                "5": ".....",
                "6": "-....",
                "7": "--...",
                "8": "---..",
                "9": "----."
                }


def main():
    if len(sys.argv) != 2:
        return print("AssertionError: the arguments are bad")
    if not check_arg():
        return print("AssertionError: the arguments are bad")
    sentence = ""
    for i in range(len(sys.argv[1])):
        sentence += NESTED_MORSE[sys.argv[1][i].capitalize()]
        if i != len(sys.argv[1]) - 1:
            sentence += " "
    print(f"{sentence}")
    return


def check_arg():
    for i in range(len(sys.argv[1])):
        if not (sys.argv[1][i].isspace() or sys.argv[1][i].isalnum()):
            return False
    return True


if __name__ == "__main__":
    main()
