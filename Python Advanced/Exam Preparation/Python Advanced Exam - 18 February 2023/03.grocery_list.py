def shop_from_grocery_list(budget: int, grocery_list: list, *info: tuple):
    for product, price in info:
        if len(grocery_list) == 0:
            break

        if product in grocery_list:
            if price > budget:
                break

            budget -= price
            grocery_list.remove(product)

    if len(grocery_list):
        return f"You did not buy all the products. Missing products: {', '.join([str(x) for x in grocery_list])}."

    return f"Shopping is successful. Remaining budget: {budget:.2f}."

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

