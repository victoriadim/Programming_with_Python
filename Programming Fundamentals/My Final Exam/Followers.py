command = input().split()
followers = {}

while command[0] != "Log":
    if command[0] == "New":
        username = command[2]
        if username not in followers:
            followers[username] = {"interactions": 0}

    elif command[0] == "Like:":
        cmd, username, likes = command[0], command[1].replace(":", ""), int(command[2])
        if username not in followers:
            followers[username] = {"interactions": likes}
        followers[username]["interactions"] = likes

    elif command[0] == "Comment:":
        username = command[1]
        if username not in followers:
            followers[username] = {"interactions": 1}
        else:
            followers[username]["interactions"] += 1

    elif command[0] == "Blocked:":
        username = command[1]
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")
    command = input().split()

print(f"{len(followers)} followers")
for username, interactions in followers.items():
    print(f"{username}: {followers[username]['interactions']}")