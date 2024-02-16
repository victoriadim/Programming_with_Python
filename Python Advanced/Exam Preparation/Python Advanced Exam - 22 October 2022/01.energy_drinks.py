from collections import deque

milligrams = deque([int(x) for x in input().split(", ")]) # last
energy_drinks = deque([int(x) for x in input().split(", ")]) # first
total_caffeine = 0

while milligrams and energy_drinks:
    current_milligrams = milligrams.pop()
    current_drink = energy_drinks.popleft()
    result = current_milligrams * current_drink
    if result <= 300 - total_caffeine:
        total_caffeine += result
    elif result > 300 - total_caffeine:
        energy_drinks.append(current_drink)
        total_caffeine -= 30
        if total_caffeine < 0:
            total_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")