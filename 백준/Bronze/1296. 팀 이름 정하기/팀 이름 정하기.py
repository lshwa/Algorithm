name = input()
n = int(input())
chars = list(name)

team_name = []
best_team = ''
best_score = -1


while n > 0:
    team = input()
    team_name.append(team)
    n -= 1


for team in team_name:
    combined = name + team

    L = combined.count('L')
    O = combined.count('O')
    V = combined.count('V')
    E = combined.count('E')

    score = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100

    if score > best_score:
        best_score = score
        best_team = team

    elif score == best_score:
        if team < best_team:
            best_team = team

print(best_team)
