from collections import deque

time = deque([int(x) for x in input().split()]) # first
tasks = deque([int(x) for x in input().split()]) # last

darth_vader_ducky = range(0, 61)
thor_ducky = range(61, 121)
big_blue_rubber_ducky = range(121, 181)
small_yellow_rubber_ducky = range(181, 241)

darth_vader_ducky_count = 0
thor_ducky_count = 0
big_blue_rubber_ducky_count = 0
small_yellow_rubber_ducky_count = 0

while time and tasks:
    current_time = time.popleft()
    current_task = tasks.pop()
    result = current_time * current_task

    if result in darth_vader_ducky:
        darth_vader_ducky_count += 1
    elif result in thor_ducky:
        thor_ducky_count += 1
    elif result in big_blue_rubber_ducky:
        big_blue_rubber_ducky_count += 1
    elif result in small_yellow_rubber_ducky:
        small_yellow_rubber_ducky_count += 1

    else:
        current_task -= 2
        tasks.append(current_task)
        time.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {darth_vader_ducky_count}\nThor Ducky: {thor_ducky_count}\n"
      f"Big Blue Rubber Ducky: {big_blue_rubber_ducky_count}\nSmall Yellow Rubber Ducky: {small_yellow_rubber_ducky_count}")