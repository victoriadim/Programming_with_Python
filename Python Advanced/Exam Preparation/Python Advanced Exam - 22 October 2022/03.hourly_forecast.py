def forecast(*info):
    result = ""
    loc_weather = {
    "Sunny": [],
    "Cloudy": [],
    "Rainy": [],
    }

    for location, weather in info:
        loc_weather[weather].append(location)

    for weather, location in loc_weather.items():
        sorted_loc = sorted(location)
        for location in sorted_loc:
            result += f"{location} - {weather}\n"

    return result[:-1]

# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))
