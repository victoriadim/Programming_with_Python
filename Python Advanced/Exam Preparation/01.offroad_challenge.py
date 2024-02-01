from collections import deque

fuel = list(map(int, input().split()))  # last
consumption_index = deque(map(int, input().split()))  # first
amount_of_fuel_needed = deque(map(int, input().split()))

altitude_levels = deque(["Altitude 1", "Altitude 2", "Altitude 3", "Altitude 4"])
reached_altitudes = []

# Your task is to take the last fuel quantity from the fuel sequence
# and the first index from the additional consumption index sequence.
# Subtract the values and check the result.

altitude_values = {}
for key in altitude_levels:
    if amount_of_fuel_needed:
        value = amount_of_fuel_needed.popleft()
        altitude_values[key] = value

while fuel and consumption_index and altitude_values:
    current_fuel = fuel[-1]
    current_consumption_index = consumption_index[0]
    current_level = altitude_levels[0]
    difference = current_fuel - current_consumption_index

    if difference >= altitude_values[current_level]:
        fuel.pop()
        consumption_index.popleft()
        reached_altitudes.append(current_level)
        del altitude_values[current_level]
        altitude_levels.popleft()
        print(f"John has reached: {current_level}")
    else:
        fuel.pop()
        consumption_index.popleft()
        altitude_levels.popleft()
        print(f"John did not reach: {current_level}")
        break

if not altitude_values:
    print(f"John has reached all the altitudes and managed to reach the top!")
else:
    print(f"John failed to reach the top.")
    if reached_altitudes:
        print(f"Reached altitudes:", ", ".join(reached_altitudes))
    else:
        print("John didn't reach any altitude.")