def team_lineup(*info) -> str:
    players_and_teams = {}
    result = []

    for player, team in info:
        if team not in players_and_teams:
            players_and_teams[team] = []
        players_and_teams[team].append(player)

    for team, players in sorted(players_and_teams.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{team}:")
        [result.append(f"  -{player}") for player in players]

    return "\n".join(result)