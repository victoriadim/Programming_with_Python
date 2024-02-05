from collections import deque

armor_monsters = deque([int(curr_armor) for curr_armor in input().split(",")])
soldier_impact = deque([int(curr_impact) for curr_impact in input().split(",")])
killed_monsters = 0

while armor_monsters and soldier_impact:
    monster = armor_monsters.popleft()
    impact = soldier_impact.pop()

    if impact >= monster:
        killed_monsters += 1
        impact -= monster
        if impact > 0:
            if not soldier_impact:
                soldier_impact.append(impact)
            else:
                soldier_impact[-1] += impact

    else:
        monster -= impact
        armor_monsters.append(monster)

if not armor_monsters:
    print(f"All monsters have been killed!")
if not soldier_impact:
    print(f"The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")