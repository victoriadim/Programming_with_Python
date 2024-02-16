def add_songs(*args):
    songs = {}

    for info in args:
        song = info[0]
        lyrics = info[1]
        if song not in songs:
            songs[song] = []
        for text in lyrics:
            songs[song].append(text)

    result = ''
    for song, lyrics in songs.items():
        result += f"- {song}\n"
        for text in lyrics:
            result += f"{text}\n"

    return result


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))