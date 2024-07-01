import sys
from ft_filter import ft_filter


def main():
    if len(sys.argv) != 3:
        return print("AssertionError: the arguments are bad")
    if not check_arg():
        return print("AssertionError: the arguments are bad")
    splited_argList = sys.argv[1].split()
    returned_list = ft_filter(checker_len, splited_argList)
    print(f'{list(returned_list)}')
    return


def checker_len(word):
    if len(word) >= int(sys.argv[2]):
        return True
    return False


def check_arg():
    for x in range(len(sys.argv[1])):
        if not (sys.argv[1][x].isalpha() or sys.argv[1][x].isspace()):
            return False
    for x in range(len(sys.argv[2])):
        if not (sys.argv[2][x].isnumeric()):
            return False
    return True


if __name__ == "__main__":
    main()
