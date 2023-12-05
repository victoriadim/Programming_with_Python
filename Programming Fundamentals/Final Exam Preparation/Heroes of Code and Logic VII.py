"""
On the first line of the standard input, you will receive an integer n – the number of heroes that you can choose for your party. On the next n lines, the heroes themselves will follow with their hit points and mana points separated by a single space in the following format:
"{hero name} {HP} {MP}"
-	HP stands for hit points and MP for mana points
-	a hero can have a maximum of 100 HP and 200 MP
After you have successfully picked your heroes, you can start playing the game. You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given.
There are several actions that the heroes can perform:
"CastSpell – {hero name} – {MP needed} – {spell name}"
•	If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message:
o	"{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
•	If the hero is unable to cast the spell print:
o	"{hero name} does not have enough MP to cast {spell name}!"
"TakeDamage – {hero name} – {damage} – {attacker}"
•	Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
o	"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
•	If the hero has died, remove him from your party and print:
o	"{hero name} has been killed by {attacker}!"
"Recharge – {hero name} – {amount}"
•	The hero increases his MP. If it brings the MP of the hero above the maximum value (200), MP is increased to 200. (the MP can't go over the maximum value).
•	 Print the following message:
o	"{hero name} recharged for {amount recovered} MP!"
"Heal – {hero name} – {amount}"
•	The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum value (100), HP is increased to 100 (the HP can't go over the maximum value).
•	 Print the following message:
o	"{hero name} healed for {amount recovered} HP!"
Input
•	On the first line of the standard input, you will receive an integer n.
•	On the following n lines, the heroes themselves will follow with their hit points and mana points separated by a space in the following format.
•	You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given.
Output
•	Print all members of your party who are still alive, in the following format (their HP/MP need to be indented 2 spaces):
"{hero name}
  HP: {current HP}
  MP: {current MP}"
Constraints
•	The starting HP/MP of the heroes will be valid, 32-bit integers will never be negative or exceed the respective limits.
•	The HP/MP amounts in the commands will never be negative.
•	The hero names in the commands will always be valid members of your party. No need to check that explicitly.
"""

number_of_heroes = int(input())
heroes = {}


def get_recovered_amount(hero_name_def, amount_type, limit):
    amount = heroes[hn][amount_type]
    heroes[hero_name_def][amount_type] += par2
    if heroes[hero_name_def][amount_type] > limit:
        heroes[hero_name_def][amount_type] = limit

    return heroes[hero_name_def][amount_type] - amount


for hero in range(1, number_of_heroes + 1):
    user_input = input().split()
    hero_name = user_input[0]
    hp = user_input[1]
    mp = user_input[2]

    heroes[hero_name] = {
        "hp": int(hp),
        "mp": int(mp)
    }

command = input().split(" – ")
while command[0] != "End":
    command = command[0].split(" - ")
    cmd, hn, par2 = command[0], command[1], int(command[2])
    if cmd == "CastSpell":
        spell_name = command[3]
        if par2 <= heroes[hn]["mp"]:
            heroes[hn]["mp"] -= par2
            print(f"{hn} has successfully cast {spell_name} and now has {heroes[hn]['mp']} MP!")
        else:
            print(f"{hn} does not have enough MP to cast {spell_name}!")

    elif cmd == "TakeDamage":
        attacker = command[3]
        heroes[hn]["hp"] -= par2
        if heroes[hn]["hp"] > 0:
            print(f"{hn} was hit for {par2} HP by {attacker} and now has {heroes[hn]['hp']} HP left!")
        else:
            heroes.pop(hn)
            print(f"{hn} has been killed by {attacker}!")

    elif cmd == "Recharge":
        amount_mp = get_recovered_amount(hn, "mp", 200)
        print(f"{hn} recharged for {amount_mp} MP!")

    elif cmd == "Heal":
        amount_hp = get_recovered_amount(hn, "hp", 100)
        print(f"{hn} healed for {amount_hp} HP!")

    command = input().split(" – ")

for hero, stats in heroes.items():
    print(f"{hero}\nHP: {stats['hp']}\nMP: {stats['mp']}")