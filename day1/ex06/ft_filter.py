def ft_filter(function, iterable):
    return [iterable[x] for x in range(len(iterable))
            if function(iterable[x]) is True]
