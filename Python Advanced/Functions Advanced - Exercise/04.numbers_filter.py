def even_odd_filter(**numbers_sets):
    if "odd" in numbers_sets:
        numbers_sets["odd"] = [n for n in numbers_sets["odd"] if n % 2 != 0]
    if "even" in numbers_sets:
        numbers_sets["even"] = [n for n in numbers_sets["even"] if n % 2 == 0]

    return dict(sorted(numbers_sets.items(), key=lambda x: -len(x[1])))