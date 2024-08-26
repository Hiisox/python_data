def callLimit(limit: int):
    """def callLimit(limit: int):
check if a function been called more than limit
Return an error if yes"""
    count = 0

    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            count += 1
            if count > limit:
                return print(f"Error: {function} call too many times")
            else:
                return function(*args, **kwds)
        return limit_function
    return callLimiter
