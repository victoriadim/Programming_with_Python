from collections import deque

worms = deque([int(worm) for worm in input().split()])
holes = deque([int(hole) for hole in input().split()])
matches = 0
worms_size = len(worms)

while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_worm <= 0:
        continue

    elif current_worm == current_hole:
        matches += 1

    elif current_worm < current_hole:
        current_worm -= 3
        if current_worm > 0:
            worms.append(current_worm)

    elif current_worm > current_hole:
        current_worm -= 3
        if current_worm > 0:
            worms.append(current_worm)

print(f"Matches: {matches}" if matches != 0 else "There are no matches.")

if worms_size == matches:
    print(f"Every worm found a suitable hole!")
elif not worms:
    print(f"Worms left: none")
elif worms:
    print(f"Worms left: ", end="")
    print(*worms, sep=", ")

if holes:
    print(f"Holes left: ", end="")
    print(*holes, sep=", ")
else:
    print("Holes left: none")