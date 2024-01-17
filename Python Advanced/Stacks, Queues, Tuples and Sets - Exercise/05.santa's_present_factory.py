from collections import deque

materials = [int(x) for x in input().split()]
magics = deque(int(x) for x in input().split())

crafted = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magics:
    material = materials.pop() if magics[0] or not materials[-1] else 0
    magic = magics.popleft() if material or not magics[0] else 0

    if not magic:
        continue

    product = material * magic

    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        materials.append(material + magic)
    elif product > 0:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")

if magics:
    print(f"Magic left: {', '.join(str(x) for x in magics)}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]