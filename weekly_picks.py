week14_picks = [
    {"team": "Detroit", "points": 64, "win": True, "favorite": True},
    {"team": "Seattle", "points": 99, "win": True, "favorite": True},
    {"team": "Buffalo", "points": 86, "win": True, "favorite": True},
    {"team": "Cleveland", "points": 94, "win": False, "favorite": True},
    {"team": "Washington", "points": 65, "win": False, "favorite": True},
    {"team": "Miami", "points": 81, "win": True, "favorite": True},
    {"team": "Tampa Bay", "points": 99, "win": False, "favorite": True},
    {"team": "Indianapolis", "points": 53, "win": False, "favorite": True},
    {"team": "Baltimore", "points": 90, "win": False, "favorite": True},
    {"team": "Denver", "points": 98, "win": True, "favorite": True},
    {"team": "Green Bay", "points": 71, "win": False, "favorite": True},
    {"team": "Los Angeles", "points": 99, "win": True, "favorite": True},
    {"team": "Kansas City", "points": 76, "win": False, "favorite": True},
    {"team": "Philadelphia", "points": 73, "win": False, "favorite": True},
]
week13_picks = [
    {
        "game": [
            {"team": "Detroit", "points": 64, "win": True, "favorite": True},
            {"team": "Dallas", "points": 36, "win": True, "favorite": False},
        ],
    },
    {
        "game": [
            {"team": "Seattle", "points": 97, "win": True, "favorite": True},
            {"team": "Atlanta", "points": 3, "win": True, "favorite": False},
        ]
    },
    {
        "game": [
            {"team": "Buffalo", "points": 86, "win": True, "favorite": True},
            {"team": "", "points": 86, "win": True, "favorite": True},
        ]
    },
    {
        "game": [
            {"team": "Cleveland", "points": 9, "win": False, "favorite": False},
            {"team": "", "points": 86, "win": True, "favorite": True},
        ]
    },
    {
        "game": [
            {"team": "Tennessee", "points": 9, "win": False, "favorite": True},
            {"team": "", "points": 86, "win": True, "favorite": True},
        ]
    },
    {
        "game": [
            {"team": "Washington", "points": 65, "win": False, "favorite": True},
            {"team": "", "points": 86, "win": True, "favorite": True},
        ]
    },
    {
        "game": [
            {"team": "Miami", "points": 81, "win": True, "favorite": True},
            {"team": "", "points": 86, "win": True, "favorite": True},
        ]
    },
    {
        "game": [
            {"team": "Tampa Bay", "points": 99, "win": False, "favorite": True},
            {"team": "", "points": 86, "win": True, "favorite": True},
        ]
    },
    {
        "game": [
            {"team": "Indianapolis", "points": 53, "win": False, "favorite": True},
            {"team": "", "points": 86, "win": True, "favorite": True},
        ]
    },
    {
        "game": [
            {"team": "Baltimore", "points": 99, "win": False, "favorite": True},
            {"team": "", "points": 86, "win": True, "favorite": True},
        ]
    },
    {
        "game": [
            {"team": "Denver", "points": 98, "win": True, "favorite": True},
            {"team": "", "points": 86, "win": True, "favorite": True},
        ]
    },
    {
        "game": [
            {"team": "Green Bay", "points": 71, "win": False, "favorite": True},
            {"team": "", "points": 86, "win": True, "favorite": True},
        ]
    },
    {
        "game": [
            {"team": "Los Angeles", "points": 99, "win": True, "favorite": True},
            {"team": "", "points": 86, "win": True, "favorite": True},
        ]
    },
    {
        "game": [
            {"team": "Kansas City", "points": 66, "win": False, "favorite": True},
            {"team": "", "points": 86, "win": True, "favorite": True},
        ]
    },
    {
        "game": [
            {"team": "Philadelphia", "points": 84, "win": False, "favorite": True},
            {"team": "", "points": 86, "win": True, "favorite": True},
        ]
    },
]
sorted_week14 = sorted(week14_picks, key=lambda k: k["points"])
sum = 0
for points, team in enumerate(sorted_week14):
    if team["win"] and team["favorite"]:
        sum += points + 1
    print(f"{team['team']:12}: {points+1:2} points")
print(f"Total Points: {sum}")
