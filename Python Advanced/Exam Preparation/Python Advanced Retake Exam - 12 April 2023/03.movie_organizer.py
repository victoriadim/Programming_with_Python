def movie_organizer(*info):
    movies = {}
    result = ''

    for movie, genre in info:
        if genre not in movies:
            movies[genre] = []

        movies[genre].append(movie)

    for genre, movie in sorted(movies.items(), key=lambda x: (-len(x[1]), x[0])):
        sorted_movies = sorted(movie)
        result += f"{genre} - {len(sorted_movies)}\n"
        for name_movie in sorted_movies:
            result += f"* {name_movie}\n"

    return result