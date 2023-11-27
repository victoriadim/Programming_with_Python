"""
On the first line, you will receive a number n. On the next n lines, you will be given some information about the plants that you have discovered in the format: "{plant}<->{rarity}". Store that information because you will need it later. If you receive a plant more than once, update its rarity.
After that, until you receive the command "Exhibition", you will be given some of these commands:
•	"Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
•	"Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
•	"Reset: {plant}" – remove all the ratings of the given plant
Note: If any given plant name is invalid, print "error"
After the command "Exhibition", print the information that you have about the plants in the following format:
"Plants for the exhibition:
- {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
- {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
…
- {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
The average rating should be formatted to the second decimal place.
Input / Constraints
•	You will receive the input as described above.
•	JavaScript: you will receive a list of strings.
Output
•	Print the information about all plants as described above.

"""


number = int(input())
plants = {}

for operation in range(number):
    plant, rarity = input().split("<->")
    if plant not in plants:
        plants[plant] = {"rarity": 0, "rating": []}
    plants[plant]["rarity"] = rarity

user_input = input()
while user_input != "Exhibition":
    command, information = user_input.split(": ")
    plant = information.split(" - ")[0]
    if plant not in plants:
        print("error")
        user_input = input()
        continue

    if command == "Rate":
        rating = int(information.split(" - ")[1])
        plants[plant]["rating"].append(rating)

    elif command == "Update":
        new_rarity = int(information.split(" - ")[1])
        plants[plant]["rarity"] = new_rarity

    elif command == "Reset":
        plant = str(information)
        plants[plant]["rating"] = []
    user_input = input()

print(f"Plants for the exhibition:")
for plant, info in plants.items():
    if len(info["rating"]) > 0:
        average_rating = sum(info["rating"]) / len(info["rating"])
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {plants[plant]['rarity']}; Rating: {average_rating:.2f}")