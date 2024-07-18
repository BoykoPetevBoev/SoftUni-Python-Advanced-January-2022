def shopping_list(budget, **kwargs):

    if budget < 100:
        return "You do not have enough budget."
    
    basket = 0
    result = []

    for product in kwargs:
        price, quantity = kwargs[product]
        total_price = price * quantity

        if total_price > budget:
            continue

        budget -= total_price
        basket += 1
        result.append(f"You bought {product} for {total_price:.2f} leva.")

        if basket == 5:
            break
    
    return "\n".join(result)


print(shopping_list(
    100, 
    microwave=(70, 2),
    skirts=(15, 4), 
    coffee=(1.50, 10)
))

print(shopping_list(
    20,
    jeans=(19.99, 1)
))

print(shopping_list(104,
    cola=(1.20, 2),
    candies=(0.25, 15),
    bread=(1.80, 1),
    pie=(10.50, 5),
    tomatoes=(4.20, 1),
    milk=(2.50, 2),
    juice=(2, 3),
    eggs=(3, 1)
))