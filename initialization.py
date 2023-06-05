from tkinter import *
from tkinter.messagebox import askyesno, showinfo
import sqlite3


class InitWindow:
    def __init__(self):
        self.window = Tk()
        self.window.title('Initialization')
        self.window.iconphoto(True, PhotoImage(file='img/initIcon.png'))

        x_coordinate = int(self.window.winfo_screenwidth() / 3 - 130)
        y_coordinate = int(self.window.winfo_screenheight() / 3 - 25)

        self.window.geometry(f'{260}x{50}+{x_coordinate}+{y_coordinate}')
        self.window.resizable(width=False, height=False)

        self.label = Label(master=self.window, text="Enter your username:")
        self.label.grid(row=0, column=0)

        self.user = Entry(master=self.window, width=10)
        self.user.grid(row=0, column=1)

        self.button = Button(master=self.window, text='Submit', command=self.check)
        self.button.grid(row=0, column=2)
        self.db = sqlite3.connect('info.db')
        self.cursor = self.db.cursor()

        self.username = None

    def run(self):
        self.window.mainloop()

    def check(self):
        entry = self.user.get()
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{entry}';")
        result = self.cursor.fetchone()
        if result is not None:
            showinfo('Enjoy', 'Successfully initialized!')
            self.username = entry
            self.window.destroy()
        else:
            if askyesno("User doesn't exist", 'Create new user?'):
                self.label.config(text='Enter new username:')
                self.button.config(command=self.create_user)
            else:
                showinfo('Ehh, see you next time', 'Have a nice day :D')
                self.window.destroy()

    def create_user(self):
        new_username = self.user.get()
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{new_username}';")
        result = self.cursor.fetchone()
        if result is None:
            self.cursor.execute(f"""CREATE TABLE "{new_username}" (
                games_played INTEGER,
                win INTEGER,
                lose INTEGER
            );""")
            self.db.commit()
            self.cursor.execute(f'INSERT INTO "{new_username}" (games_played, win, lose) VALUES (0, 0, 0);')
            self.db.commit()
            showinfo('Enjoy', 'Player has been successfully created!')
            self.username = new_username
            self.window.destroy()
        else:
            showinfo('Already exists', 'Enter another username')
