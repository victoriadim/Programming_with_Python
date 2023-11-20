inventory = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break

    if "Combine Items" in command:
        command_type = command.split(" - ")
        old_item, new_item = command_type[1].split(":")
        if old_item in inventory:
            inventory.insert(inventory.index(old_item) + 1, new_item)
        continue

    command_type, item = command.split(" - ")
    if command_type == "Collect":
        if item not in inventory:
            inventory.append(item)
    elif command_type == "Drop":
        if item in inventory:
            inventory.remove(item)
    elif command_type == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

print(*inventory, sep=", ")