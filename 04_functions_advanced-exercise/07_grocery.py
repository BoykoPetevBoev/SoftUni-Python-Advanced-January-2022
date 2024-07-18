def grocery_store(**kwargs):
    result = []

    data = sorted(kwargs.items(), key=lambda kwp: ( kwp[1], len(kwp[0])), reverse=True)
    # data = sorted(data, key=lambda kwp: kwp[1], reverse=True)

    for key, value in data:
        result.append(f"{key}: {value}")
    return "\n".join(result)

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
