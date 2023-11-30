import re

user_input = input()
calories = 0
result = []
pattern = re.compile(r"([#|])(?P<item>[A-Za-z\s]+)\1(?P<expiration_date>[0-9]{2}/[0-9]{2}/[0-9]{2})\1(?P<calories>[0-9]+)\1")

matches = re.finditer(pattern, user_input)
for match in matches:
    current_cal = int(match["calories"])
    calories += current_cal
    result.append({"name": match["item"], "date": match["expiration_date"], "nutrition": match["calories"]})
number_day = calories // 2000
print(f"You have food to last you for: {number_day} days!")
if number_day > 0:
    for match in result:
        print(f'Item: {match["name"]}, Best before: {match["date"]}, Nutrition: {match["nutrition"]}')