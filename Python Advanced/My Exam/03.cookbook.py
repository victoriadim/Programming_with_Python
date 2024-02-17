def cookbook(*info):
    recipes = {}
    result = ''

    for recipe, cuisine, ingredients in info:
        if cuisine not in recipes:
            recipes[cuisine] = []
        recipes[cuisine].append((recipe, ingredients))

    sort_by_cuisines = sorted(recipes.keys(), key=lambda x: (-len(recipes[x]), x))
    for cuisine in sort_by_cuisines:
        result += f"{cuisine} cuisine contains {len(recipes[cuisine])} recipes:\n"
        sorted_recipes = sorted(recipes[cuisine], key=lambda x: x[0])
        for recipe, ingredients in sorted_recipes:
            result += f"  * {recipe} -> Ingredients: {', '.join(ingredients)}\n"

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
