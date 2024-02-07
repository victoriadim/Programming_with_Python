def accommodate_new_pets(capacity, maximum_weight, *info):
    pets = {}
    result = ''

    for pet, weight in info:
        if not capacity:
            result += "You did not manage to accommodate all pets!\n"
            break
        if weight > maximum_weight:
            continue
        if pet not in pets:
            pets[pet] = 0
        pets[pet] += 1
        capacity -= 1

    else:
        result += f"All pets are accommodated! Available capacity: {capacity}.\n"

    result += "Accommodated pets:\n"
    for pet, count in sorted(pets.items()):
        result += f"{pet}: {count}\n"

    return result
