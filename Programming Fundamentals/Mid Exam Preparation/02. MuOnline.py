room = input().split("|")
health = 100
bitcoins = 0
count_rooms = 0

for command in room:
    command_type, number = command.split()
    amount = int(number)
    count_rooms += 1
    if command_type == "potion":
        if health + amount > 100:
            amount = 100 - health
        health += amount
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")

    elif command_type == "chest":
        bitcoins += amount
        print(f"You found {amount} bitcoins.")

    else:
        health -= amount
        if health > 0:
            print(f"You slayed {command_type}.")
        else:
            print(f"You died! Killed by {command_type}.")
            print(f"Best room: {count_rooms}")
            break

if health > 0:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")