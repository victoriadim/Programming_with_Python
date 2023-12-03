import re


number_of_inputs = int(input())
for i in range(number_of_inputs):
    inputs = input()
    pattern = r"\|(?P<name>[A-Z]{1,})\|:#(?P<position>[A-Z][a-z]{1,} [A-Za-z]{1,})#"
    matches = re.findall(pattern, inputs)
    for match in matches:
        current_name = match[0]
        current_position = match[1]
        print(f"{current_name}, The {current_position}\n>> Strength: {len(current_name)}\n>> Armor: {len(current_position)}")
    if not matches:
        print("Access denied!")