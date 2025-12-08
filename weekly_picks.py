week14_picks = [
    {"team": "Detroit", "points": 64, "win": True},
    {"team": "Seattle", "points": 99, "win": True},
    {"team": "Buffalo", "points": 86, "win": True},
    {"team": "Cleveland", "points": 94, "win": False},
    {"team": "Washington", "points": 65, "win": False},
    {"team": "Miami", "points": 81, "win": True},
    {"team": "Tampa Bay", "points": 99, "win": False},
    {"team": "Indianapolis", "points": 53, "win": False},
    {"team": "Baltimore", "points": 90, "win": False},
    {"team": "Denver", "points": 98, "win": True},
    {"team": "Green Bay", "points": 71, "win": False},
    {"team": "Los Angeles", "points": 99, "win": True},
    {"team": "Kansas City", "points": 76, "win": False},
    {"team": "Philadelphia", "points": 73, "win": False},
]
sorted_week14 = sorted(week14_picks, key=lambda k: k["points"])
sum = 0
for points, team in enumerate(sorted_week14):
    if team["win"]:
        sum += points + 1
    print(f"{team['team']:12}: {points+1:2} points")
print(sum)
