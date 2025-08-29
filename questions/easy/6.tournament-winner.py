# Tournament Winner 🟢
# There's a tournament taking place. Given an array of competitions and results, determine who the winner is
# Each victory sums 3 points, there's always a winner, no ties are allowed
# There will always be at least two teams
# 0 represents the away team won, 1 represents the home team won


# Space Complexity On where n is the number of teams
# Time Complexity Ok where k is the number of results
def tournament_winner(competitions, results):
    scores = {}
    max_score = 0
    winner = ""
    round_winner = ""
    for index, result in enumerate(results):
        teams = competitions[index]
        home_team = teams[0]
        away_team = teams[1]

        if home_team not in scores:
            scores[home_team] = 0
        if away_team not in scores:
            scores[away_team] = 0

        round_winner = away_team if result == 0 else home_team
        scores[round_winner] += 3

        if scores[round_winner] > max_score:
            max_score = scores[round_winner]
            winner = round_winner

    return winner

print(tournament_winner([["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]], [0, 0, 1]))
print(tournament_winner([["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]], [0, 1, 1]))
print(tournament_winner([["HTML", "Java"], ["Java", "Python"], ["Python", "HTML"]], [0, 1, 0]))