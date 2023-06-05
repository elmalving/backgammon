from GUI.menu import Menu
from GUI.stats import Stats
from GUI.mode import Mode
from GUI.game import Game
from userStats import User


class Logic:
    def __init__(self):
        self.current_menu = Menu()

    def run(self):
        while self.current_menu:
            self.current_menu.show()
            selected_option = self.current_menu.current_window
            if selected_option == 'Menu':
                self.current_menu = Menu()
            elif selected_option == 'Stats':
                self.current_menu = Stats()
            elif selected_option == 'Mode':
                self.current_menu = Mode()
            elif selected_option == 'duo' or selected_option == 'computer':
                self.current_menu = Game(selected_option)
            else:
                self.current_menu = False


# initializing user
# starting up the game
if __name__ == "__main__":
    user = User()
    game = Logic()
    game.run()
