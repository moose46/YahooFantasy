# This is a sample Python script.
import sqlite3
from sqlite3 import Cursor
from nfl_data import teams, teamsjson, divisionsjson

# https://www.baltimoreravens.com/


# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
conn = sqlite3.connect("YahooFantasy.db")

cursor: Cursor = conn.cursor()
cursor.execute(f"drop table if exists teams")
cursor.execute(f"drop table if exists nfl_division")


def create_Tables(team):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {team}")  # Press F9 to toggle the breakpoint.
    # cursor.execute(
    #     f"create table if not exists nfl_division (id integer primary key autoincrement not null, division_name text)"
    # )
    # https://sqlite.org/foreignkeys.html
    # cursor.execute(
    #     f"CREATE TABLE IF NOT EXISTS {team} (id integer primary key autoincrement not null, team_name text not null, wins integer default 0, losses integer default 0, nfldivision integer, FOREIGN KEY(nfldivision) REFERENCES nfl_division(id))"
    # )
    cursor.execute(
        f"create table if not exists teams (id integer primary key autoincrement not null, team_name text not null, division text not null, wins integer not null default 0, losses integer not null default 0, ties integer not null default 0)"
    )


def insert_into_team(name):
    print(f"Hi, {name}")
    try:
        cursor.execute(
            f"INSERT INTO teams (team_name, division, wins, losses, ties) VALUES (?,?,?,?,?)",
            (
                name["name"],
                name["Division"],
                name["Wins"],
                name["Losses"],
                name["Ties"],
            ),
        )
    except sqlite3.IntegrityError as e:
        print(f"{e}")


# Press the green button in the gutter to run the script.
# https://docs.python.org/3.12/library/sqlite3.html#sqlite3-placeholders
def create_Divisions(divisionsjson):
    try:
        cursor.executemany(
            "INSERT INTO nfl_division (division_name) VALUES (:name)", divisionsjson
        )
    except sqlite3.IntegrityError as e:
        print(f"{e}")
        exit()


if __name__ == "__main__":
    create_Tables("team")
    # create_Divisions(divisionsjson)
    for team in teamsjson:
        insert_into_team(team)

    conn.commit()
    # nfldivision = cursor.execute("select * from PyCharm")
    # for division in nfldivision:
    #     print(division)
    cursor.close()
    conn.close()
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
