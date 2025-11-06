# This is a sample Python script.
# import sqlite3
# from sqlite3 import Cursor
import sys

from nfl_data import teamsjson
from json_data.nfl_schedule import team
import psycopg
import psycopg_binary

# https://www.baltimoreravens.com/S

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# conn = sqlite3.connect("YahooFantasy.db")
try:
    conn = psycopg.connect(
        dbname="Football", user="bob", password="admin", host="localhost", port=5432
    )
except psycopg.OperationalError:
    print("Database connection failed.")
    sys.exit(1)

with conn.cursor() as cur:
    cur.execute(f"drop table if exists teams")
    cur.execute(f"drop table if exists divisions")
    conn.commit()


def create_Tables(team):
    # Use a breakpoint in the code line below to debug your script.
    print(f"Hi, {team}")  # Press F9 to toggle the breakpoint.
    with conn.cursor() as cur:
        cur.execute(
            f"create table if not exists divisions (id serial primary key not null, name varchar not null, CONSTRAINT division_unique UNIQUE (name))"
        )
        # cur.execute(
        #     f"create table if not exists nfl_division (id serial primary key not null, division_name text)"
        # )
        # https://sqlite.org/foreignkeys.html
        # cursor.execute(
        #     f"CREATE TABLE IF NOT EXISTS {team} (id integer primary key autoincrement not null, team_name text not null, wins integer default 0, losses integer default 0, nfldivision integer, FOREIGN KEY(nfldivision) REFERENCES nfl_division(id))"
        # )
        cur.execute(
            f"create table if not exists teams (id serial primary key not null, team_name varchar not null, division varchar not null, wins int not null default 0, losses int not null default 0, ties int not null default 0,pct float4, www varchar)"
        )


def insert_into_team(name):
    print(f"Hi, {name}")
    try:
        with conn.cursor() as cur:
            cur.execute(
                f"INSERT INTO teams (team_name, division, wins, losses, ties, pct, www) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (
                    name["team_name"],
                    name["division"],
                    name["wins"],
                    name["losses"],
                    name["ties"],
                    round(name["wins"] / (name["wins"] + name["losses"]), 3),
                    name["www"],
                ),
            )
    except psycopg.OperationalError as e:
        print(f"{e}")


def insert_into_matches(name):
    print(f"Hi, {name}")
    try:
        with conn.cursor() as cur:
            cur.execute(
                f"INSERT INTO matches (team_name, division, wins, losses, ties, pct, www) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (
                    name["team_name"],
                    name["division"],
                    name["wins"],
                    name["losses"],
                    name["ties"],
                    round(name["wins"] / (name["wins"] + name["losses"]), 3),
                    name["www"],
                ),
            )
    except psycopg.OperationalError as e:
        print(f"{e}")


if __name__ == "__main__":
    create_Tables("team")
    for team in teamsjson:
        insert_into_team(team)

    conn.commit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
