def ft_statistics(*args: any, **kwargs: any) -> None:
    if checker(args, kwargs) is False:
        print("ERROR")
    myList = [x for x in args]
    myList.sort()
    # mean(mylist)
    # median(mylist)
    # quartile(mylist)
    # var(myList)


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
    return mean


def median(myList: list):
    index = len(myList)
    print(index % 2)
    if index % 2 != 0:
        index = int(index / 2 - 0.5)
        print(myList[index])
    else :
        index = int(index / 2 - 1)
        return (myList[index] + myList[index + 1]) / 2


def quartile(myList: list):
    value = len(myList)
    value2 = value
    value2 = value2/ 4
    quartile = []
    value2 = int(value2)
    quartile.append(myList[value2])
    value2 = (3 * value)/ 4
    value2 = int(value2)
    quartile.append(myList[value2])
    return quartile



def var(myList: list):
    mean = mean(myList)
    var = 0
    for value in myList:
        x = value - mean
        var = var + x * x
    var = var / (len(myList))
    return var


def racine_carre(number: float):
    print(str(number), type(str(number)))
    pass

# ft_statistics(5, 75, 450, 18, 597, 27474, 48575)
racine_carre(10.42)