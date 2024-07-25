
def checker(*args:any, **kwargs:any) -> bool:
    for x in args[0]:
        if type(x) not in [int, float]:
            return False
    return True


def mean(myList: list):
    mean = 0
    for x in myList:
        mean += x
    mean /= len(myList)
    print(mean)


def median(myList: list):
    index = len(myList)
    print(index % 2)
    if index % 2 != 0:
        index = int(index / 2 - 0.5)
        print(myList[index])
    else :
        index = int(index / 2 - 1)
        print((myList[index] + myList[index + 1]) / 2)


def quartile(myList: list):
    value = len(myList)
    value2 = value
    value2 = (value2 + 1)/ 4
    quartile = []
    if value2 == int(value2):
        quartile.append(myList[value2 - 1])
    else:
        print(value2)
        x = value2
        while (x > 1):
            x -= 1
        value2 = int(value2)
        quartile.append((1 - x) * myList[value2 - 1] + x * myList[value2])
    value2 = 3 * ((value + 1 )/ 4)
    if value2 == int(value2):
        quartile.append(myList[value2 - 1])
    else:
        x = value2
        while (x > 1):
            x -= 1
        value2 = int(value2)
        quartile.append((1 - x) * myList[value2 - 1] + x * myList[value2])
    print(quartile)


def ft_statistics(*args: any, **kwargs: any) -> None:
    if checker(args, kwargs) is False:
        print("ERROR")
    mylist = [x for x in args]
    mylist.sort()
    # mean(mylist)
    # median(mylist)
    quartile(mylist)

    return


ft_statistics(1, 11, 42, 64, 360)