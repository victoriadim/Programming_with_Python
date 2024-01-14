n = int(input())
cars = set()

for _ in range(n):
    data = input().split(", ")
    direction, car_number = data

    if direction == "IN":
        cars.add(car_number)
    elif direction == "OUT":
        cars.remove(car_number)

if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")