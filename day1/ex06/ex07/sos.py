import sys

NESTED_MORSE = { " ": "/",
                "A" : ".-",
                "B" : "-...",
                "C" : "-.-.",
                "D" : "-..",
                "E" : ".",
                "F" : "..-.",
                "G" : "--.",
                "H" : "....",
                "I" : "..",
                "J" : ".---",
                "K" : "-.-",
                "L" : ".-..",
                "M" : "--",
                "N" : "-.",
                "O" : "---",
                "P" : ".--.",
                "Q" : "--.-",
                "R" : ".-.",
                "S" : "...",
                "T" : "-",
                "U" : "..-",
                "V" : "...-",
                "W" : ".--",
                "X" : "-..-",
                "Y" : "-.--",
                "Z" : "--..",
                "0" : "-----",
                "1" : ".----",
                "2" : "..---",
                "3" : "...--",
                "4" : "....-",
                "5" : ".....",
                "6" : "-....",
                "7" : "--...",
                "8" : "---..",
                "9" : "----."
                }
def main():
    if len(sys.argv) != 2:
        return print("AssertionError: the arguments are bad")
    if not check_arg():
        return print("AssertionError: the arguments are bad")
    sentense = ""
    for i in range(len(sys.argv[1])):
        sentense += NESTED_MORSE(sys.argv[1][i])
        if not i == len(sys.argv[1])
            sentense += " "
    return


def check_arg():
    for x in range(len(sys.argv[1])):
        if not (sys.argv[1][x].isalnum() or sys.argv[1][x].isspace()):
            return False
    return True


if __name__ == "__main__":
    main()