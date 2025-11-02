# This is a sample Python script.
import sqlite3
from sqlite3 import Cursor
from nfl_data import teams


# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
conn = sqlite3.connect("YahooFantasy.db")

cursor: Cursor = conn.cursor()
cursor.execute(f"drop table if exists PyCharm")
cursor.execute(f"drop table if exists nfl_division")


def create_Tables(team):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {team}")  # Press F9 to toggle the breakpoint.
    cursor.execute(
        f"create table if not exists nfl_division (id integer primary key autoincrement not null, division_name text)"
    )
    # https://sqlite.org/foreignkeys.html
    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {team} (id integer primary key autoincrement not null, team_name text not null, wins integer default 0, losses integer default 0, nfldivision integer, FOREIGN KEY(nfldivision) REFERENCES nfl_division(id))"
    )


def insert_into_team(name):
    print(f"Hi, {name}")
    try:
        cursor.execute(f"INSERT INTO PyCharm (team_name) VALUES (?)", (name,))
    except sqlite3.IntegrityError as e:
        print(f"{e}")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    create_Tables("PyCharm")
    for team in teams:
        insert_into_team(team)

    cursor.close()
    conn.commit()
    conn.close()
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
