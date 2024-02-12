from collections import deque

textiles = deque(int(x) for x in input().split()) # take the first
medicaments = deque(int(x) for x in input().split()) # take the last

sum_items = {
    "Patch": 0, # 30
    "Bandage": 0, # 40
    "MedKit": 0 # 100
}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()

    item = current_textile + current_medicament

    if item == 30:
        sum_items["Patch"] += 1
    elif item == 40:
        sum_items["Bandage"] += 1
    elif item == 100:
        sum_items["MedKit"] += 1
    elif item > 100:
        sum_items["MedKit"] += 1
        medicaments[-1] += item - 100
    else:
        medicaments.append(current_medicament + 10)

sorted_items = sorted(sum_items.items(), key=lambda x: (-x[1], x[0]))

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
    for item in sorted_items:
        if item[1] > 0:
            print(f"{item[0]} - {item[1]}")

elif not textiles:
    print("Textiles are empty.")
    for item in sorted_items:
        if item[1] > 0:
            print(f"{item[0]} - {item[1]}")

    medicaments = reversed(medicaments)
    print(f"Medicaments left: {', '.join([str(x) for x in medicaments])}")

elif not medicaments:
    print("Medicaments are empty.")
    for item in sorted_items:
        if item[1] > 0:
            print(f"{item[0]} - {item[1]}")
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")