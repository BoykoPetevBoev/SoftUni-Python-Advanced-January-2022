def even_odd_filter(**kwargs):
    result = {}
    sorted_args = sorted(kwargs.items(), key=lambda kvp: len(kvp[1]), reverse=True)
    for key, value in sorted_args:
        if (key == "even"):
            result[key] = list(filter(lambda x: x % 2 == 0, value))
        elif (key == "odd"):
            result[key] = list(filter(lambda x: x % 2 == 1, value))
    return result


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
