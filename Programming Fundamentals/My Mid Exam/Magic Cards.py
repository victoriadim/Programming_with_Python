"""
Create a program that adds, inserts, removes, and swaps cards in a new deck. On the first line, you will receive all cards in the original deck, separated by ":". Until you receive the "Ready" command, you will get commands in the format:
•	"Add {cardName}":
o	If the card exists in the original deck, add the card to the end of the new deck.
o	Otherwise, print "Card not found."
•	"Insert {cardName} {index}":
o	If the card exists in the original deck and the index (in the new deck) is valid, insert the card at the given index of the new deck.
o	If the card does not exist in the original deck or the index (in the new deck) is invalid, print "Error!"
•	"Remove {cardName}":
o	If the card exists in the new deck, remove it.
o	Otherwise, print "Card not found."
•	"Swap {cardName1} {cardName2}":
o	Swap the positions of the cards in the new deck.
o	Input will always be valid.
•	"Shuffle deck":
o	Reverse the new deck.
When you receive the "Ready" command, print the cards in the new deck, separated by a single space.
Input / Constraints
•	On the first line, you will receive the arsenal of all cards available separated by ":".
•	On the following lines, until you receive the "Ready" command, you will receive commands to arrange your deck.
•	An index is valid when it is non-negative and less than the size of the collection.
"""
cards = input().split(":")
commands = input().split()
new_deck = []

while commands[0] != "Ready":
    if commands[0] == "Add":
        card_name = commands[1]
        if card_name in cards:
            cards.remove(card_name)
            new_deck.append(card_name)
        else:
            print("Card not found.")
    elif commands[0] == "Insert":
        card_name = commands[1]
        index = int(commands[2])
        if card_name in cards and 0 <= index < len(new_deck):
            new_deck.insert(index, card_name)
        else:
            print("Error!")
    elif commands[0] == "Remove":
        card_name = commands[1]
        if card_name in new_deck:
            new_deck.remove(card_name)
        else:
            print("Card not found.")
    elif commands[0] == "Swap":
        first_card = commands[1]
        second_card = commands[2]
        first, second = new_deck.index(first_card), new_deck.index(second_card)
        new_deck[second], new_deck[first] = new_deck[first], new_deck[second]
    elif commands[0] == "Shuffle":
        if commands[1] == "deck":
            new_deck.reverse()
    commands = input().split()

print(*new_deck, sep=" ")