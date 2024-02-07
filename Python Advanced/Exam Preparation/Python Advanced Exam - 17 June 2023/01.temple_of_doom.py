from collections import deque

tools = deque([int(x) for x in input().split()]) # take the first
substances = deque([int(x) for x in input().split()]) # take the last
challenges = deque([int(x) for x in input().split()])

while True:

    if (not tools or not substances) and challenges:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break

    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

    current_tool = tools.popleft()
    current_substance = substances.pop()
    result = current_tool * current_substance

    for challenge in challenges:
        if result == challenge:
            challenges.remove(challenge)
            break

    else:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1
        if current_substance > 0:
            substances.append(current_substance)

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")