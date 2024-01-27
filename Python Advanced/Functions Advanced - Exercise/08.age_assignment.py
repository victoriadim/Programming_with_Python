def age_assignment(*names, **age_data):
    result = []

    for letter, age in age_data.items():
        for name in names:
            if name.startswith(letter):
                result.append(f"{name} is {age} years old.")
                break

    return "\n".join(sorted(result))