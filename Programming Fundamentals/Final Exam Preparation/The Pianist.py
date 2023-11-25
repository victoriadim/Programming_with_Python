number_of_pieces = int(input())
pieces_collection = {}

for piece in range(number_of_pieces):
    pieces = input().split("|")
    name = pieces[0]
    composer = pieces[1]
    key = pieces[2]
    pieces_collection[name] = [composer, key]

while True:
    command_type = input().split("|")

    if command_type[0] == "Stop":
        break

    elif command_type[0] == "Add":
        piece = command_type[1]
        composer = command_type[2]
        key = command_type[3]
        if piece not in pieces_collection.keys():
            pieces_collection[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif command_type[0] == "Remove":
        piece = command_type[1]
        if piece in pieces_collection.keys():
            pieces_collection.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command_type[0] == "ChangeKey":
        piece = command_type[1]
        new_key = command_type[2]
        if piece in pieces_collection.keys():
            pieces_collection[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, values in pieces_collection.items():
    print(f"{piece} -> Composer: {values[0]}, Key: {values[1]}")