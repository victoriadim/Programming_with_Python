food_in_kilograms = float(input())
hay_in_kilograms = float(input())
cover_in_kilograms = float(input())
weight_in_kilograms = float(input())

for day in range(1, 31):
    food_in_kilograms -= 0.3
    if day % 2 == 0:
        hay_in_kilograms -= 0.05 * food_in_kilograms
    if day % 3 == 0:
        cover_in_kilograms -= weight_in_kilograms / 3
    if food_in_kilograms < 0 or hay_in_kilograms < 0 or cover_in_kilograms < 0:
        print(f"Merry must go to the pet store!")
        break

if food_in_kilograms > 0 and hay_in_kilograms > 0 and cover_in_kilograms > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food_in_kilograms:.2f}, Hay: {hay_in_kilograms:.2f}, Cover: {cover_in_kilograms:.2f}.")