week14_picks = [
    {"team": "Detroit", "points": 64},
    {"team": "Seattle", "points": 99},
    {"team": "Buffalo", "points": 86},
    {"team": "Cleveland", "points": 94},
    {"team": "Washington", "points": 65},
    {"team": "Miami", "points": 81},
    {"team": "Tampa Bay", "points": 99},
    {"team": "Indianapolis", "points": 53},
    {"team": "Baltimore", "points": 90},
    {"team": "Denver", "points": 98},
    {"team": "Green Bay", "points": 71},
    {"team": "Los Angeles", "points": 99},
    {"team": "Kansas City", "points": 76},
    {"team": "Philadelphia", "points": 73},
]
sorted_week14 = sorted(week14_picks, key=lambda k: k["points"])
for points, team in enumerate(sorted_week14):
    print(f"{team['team']:12}: {points+1:2} points")
