from collections import deque

food = deque(int(x) for x in input().split(", ")) # take the last
stamina = deque(int(x) for x in input().split(", ")) # take the first

peak_names = ["Vihren", "Kutelo", "Banski Suhodol", "Polezhan", "Kamenitza"]
peak_values = [80, 90, 100, 60, 70]
days = 0
climbed_peaks = []

while days < 7:
    if food and stamina:
        current_food = food.pop()
        current_stamina = stamina.popleft()
        result = current_food + current_stamina

        if peak_values:
            if result >= peak_values[0]:
                climbed_peaks.append(peak_names[0])
                peak_names.pop(0)
                peak_values.pop(0)
        else:
            break
    else:
        break

    days += 1

if len(climbed_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if climbed_peaks:
    print(f"Conquered peaks: ")
    for peak in climbed_peaks:
        print(peak)