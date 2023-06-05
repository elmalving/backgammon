import initialization
import sqlite3


class User:
    def __init__(self):
        __player = initialization.InitWindow()
        __player.run()
        if not __player.username:
            exit()
        self.name = __player.username

        db = sqlite3.connect('info.db')
        cursor = db.cursor()

        cursor.execute(f'SELECT win FROM "{self.name}"')
        db.commit()
        win = cursor.fetchone()
        self.win = win[0]

        cursor.execute(f'SELECT lose FROM "{self.name}"')
        db.commit()
        lose = cursor.fetchone()
        self.lose = lose[0]

        self.games_played = self.win + self.lose
