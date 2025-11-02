# This is a sample Python script.
import sqlite3
from sqlite3 import Cursor

teams = ["Baltimore","Miami","Chicago","Cincinnati","Detroit","Minnesota", "Green Bay","Carolina","Los Angeles (LAC)","Tennessee","New England","Atlanta","San Francisco","New York Giants (NYG)","Indianapolis","Pittsburgh","Houston","Denver","Jacksonville","Las Vegas","Los Angeles (LAR)", "New Orleans","Kansas City","Buffalo","Seattle","Washington","Dallas","Arizona"]
# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
conn = sqlite3.connect('YahooFantasy.db')

cursor: Cursor = conn.cursor()
cursor.execute(f'drop table PyCharm')
def create_Tables(team):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {team}')  # Press F9 to toggle the breakpoint.
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {team} (id integer primary key autoincrement not null, team_name text not null)')

def insert_into_team(name):
    print(f'Hi, {name}')
    try:
        cursor.execute(f'INSERT INTO PyCharm (team_name) VALUES (?)', (name,))
    except sqlite3.IntegrityError as e:
        print(f'{e}')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_Tables('PyCharm')
    for team in teams:
        insert_into_team(team)

    cursor.close()
    conn.commit()
    conn.close()
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
