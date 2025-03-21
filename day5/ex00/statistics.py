def ft_statistics(*args: any, **kwargs: any) -> None:
    """Check if args are valids then call the fonction \
print_arg"""
    if checker(args, kwargs) is False:
        print("ERROR")
        return
    myList = [x for x in args]
    myList.sort()
    print_arg(myList, kwargs)


def print_arg(myList: list, kwargs: dict):
    """Check which arguments need to be called then call \
the fonctions"""
    str_tab = ["mean", "median", "quartile", "var", "std"]
    function_tab = [mean, median, quartile, var, std]
    for key in kwargs:
        x = 0
        for index in str_tab:
            if kwargs[key] == index:
                print(function_tab[x](myList))
            x += 1
    return


def checker(*args: any, **kwargs: any) -> bool:
    """checker fonction"""
    for x in args[0]:
        if type(x) not in [int, float]:
            return False
    return True


def mean(myList: list):
    """return the mean of a list"""
    if len(myList) == 0:
        return "ERROR"
    mean = 0
    for x in myList:
        mean += x
    mean /= len(myList)
    return mean


def median(myList: list):
    """return the median of a fonction"""
    if len(myList) == 0:
        return "ERROR"
    index = len(myList)
    if index % 2 != 0:
        index = int(index / 2 - 0.5)
        return myList[index]
    else:
        index = int(index / 2 - 1)
        return (myList[index] + myList[index + 1]) / 2


def quartile(myList: list):
    """return the quartile of a list"""
    if len(myList) == 0:
        return "ERROR"
    value = len(myList)
    value2 = value
    value2 = value2 / 4
    quartile = []
    value2 = int(value2)
    quartile.append(myList[value2])
    value2 = (3 * value) / 4
    value2 = int(value2)
    quartile.append(myList[value2])
    return quartile


def var(myList: list):
    """return the var of a list"""
    if len(myList) == 0:
        return "ERROR"
    mean_var = mean(myList)
    var = 0
    for value in myList:
        x = value - mean_var
        var = var + x * x
    var = var / (len(myList))
    return var


def std(myList: list):
    """return the std of a list"""
    if len(myList) == 0:
        return "ERROR"
    return var(myList) ** 0.5
