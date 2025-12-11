from datetime import date

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
            {"team": "Tampa Bay", "points": 97, "win": False, "favorite": True},
            {"team": "Atlanta", "points": 3, "win": False, "favorite": False},
            {"date": date(2025, 12, 11)},
        ],
    },
    {
        "game": [
            {"team": "Chicago", "points": 97, "win": False, "favorite": True},
            {"team": "Cleveland", "points": 3, "win": False, "favorite": False},
            {"date": date(2025, 12, 14)},
        ],
    },
    {
        "game": [
            {"team": "Baltimore", "points": 26, "win": False, "favorite": False},
            {"team": "Cincinnati", "points": 74, "win": False, "favorite": False},
            {"date": date(2025, 12, 14)},
        ]
    },
    {
        "game": [
            {"team": "Cleveland", "points": 9, "win": False, "favorite": False},
            {"team": "", "points": 86, "win": False, "favorite": False},
            date(2025, 12, 14),
        ]
    },
    {
        "game": [
            {"team": "Tennessee", "points": 9, "win": False, "favorite": False},
            {"team": "", "points": 86, "win": False, "favorite": False},
            date(2025, 12, 14),
        ]
    },
    {
        "game": [
            {"team": "Washington", "points": 65, "win": False, "favorite": False},
            {"team": "", "points": 86, "win": False, "favorite": False},
            date(2025, 12, 14),
        ]
    },
    {
        "game": [
            {"team": "Miami", "points": 81, "win": False, "favorite": False},
            {"team": "", "points": 86, "win": False, "favorite": False},
            date(2025, 12, 14),
        ]
    },
    {
        "game": [
            {"team": "Tampa Bay", "points": 99, "win": False, "favorite": False},
            {"team": "", "points": 86, "win": False, "favorite": False},
            date(2025, 12, 14),
        ]
    },
    {
        "game": [
            {"team": "Indianapolis", "points": 53, "win": False, "favorite": False},
            {"team": "", "points": 86, "win": False, "favorite": False},
            date(2025, 12, 14),
        ]
    },
    {
        "game": [
            {"team": "Baltimore", "points": 99, "win": False, "favorite": False},
            {"team": "", "points": 86, "win": False, "favorite": False},
            date(2025, 12, 14),
        ]
    },
    dict(
        game=[
            {"team": "Denver", "points": 98, "win": False, "favorite": False},
            {"team": "", "points": 86, "win": False, "favorite": False},
            date(2025, 12, 14),
        ]
    ),
    dict(
        game=[
            {"team": "Green Bay", "points": 71, "win": False, "favorite": False},
            {"team": "", "points": 86, "win": False, "favorite": False},
            date(2025, 12, 14),
        ]
    ),
    dict(
        game=[
            {"team": "Los Angeles", "points": 99, "win": False, "favorite": False},
            {"team": "", "points": 86, "win": False, "favorite": False},
            date(2025, 12, 14),
        ]
    ),
    {
        "game": [
            {"team": "Kansas City", "points": 66, "win": False, "favorite": False},
            {"team": "", "points": 86, "win": False, "favorite": False},
            date(2025, 12, 14),
        ]
    },
    {
        "game": [
            {"team": "Pittsburg", "points": 87, "win": False, "favorite": False},
            {"team": "Miami", "points": 13, "win": False, "favorite": False},
            date(2025, 12, 15),
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
