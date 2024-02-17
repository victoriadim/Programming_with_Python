from collections import deque

money = deque([int(x) for x in input().split()])
prices = deque([int(x) for x in input().split()])
foods = 0

while money and prices:
    current_money = money.pop()
    current_prices = prices.popleft()

    if current_money == current_prices:
        foods += 1

    elif current_money > current_prices:
        change = current_money - current_prices
        money.appendleft(current_money)
        money[-1] += change
        foods += 1

    elif current_money < current_prices:
        continue

if foods >= 4:
    print(f"Gluttony of the day! Henry ate {foods} foods.\n")
elif 1 < foods < 4:
    print(f"Henry ate: {foods} foods.")
elif foods == 1:
    print(f"Henry ate: {foods} food.")
elif foods == 0:
    print(f"Henry remained hungry. He will try next weekend again.")