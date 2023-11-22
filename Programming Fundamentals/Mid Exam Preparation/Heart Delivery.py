neighborhood = [int(x) for x in input().split("@")]
command = input()
house_index = 0
len_neighborhood = len(neighborhood)

while command != "Love!":
    command_type, number = command.split()
    house_index += int(number)
    if house_index > len_neighborhood - 1:
        house_index = 0
    if neighborhood[house_index] >= 2:
        neighborhood[house_index] -= 2
        if neighborhood[house_index] == 0:
            print(f"Place {house_index} has Valentine's day.")
    else:
        if neighborhood[house_index] == 0:
            print(f"Place {house_index} already had Valentine's day.")
    command = input()

print(f"Cupid's last position was {house_index}.")
count_house = neighborhood.count(0)
if count_house == len_neighborhood:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len_neighborhood - count_house} places.")