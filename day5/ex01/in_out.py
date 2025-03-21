def square(x: int | float) -> int | float:
    """def square(x: int | float) -> int | float: \
return the square of the arg x"""
    return x * x


def pow(x: int | float) -> int | float:
    """def pow(x: int | float) -> int | float: \
return the power of the arg x"""
    return x ** x


def outer(x: int | float, function) -> object:
    """def outer(x: int | float, function) -> object: \
return a callable object that will return the result \
of his own previous call"""
    count = 0

    def inner() -> float:
        nonlocal count
        count += 1
        result = x
        for y in range(count):
            result = function(result)
        return result
    return inner
