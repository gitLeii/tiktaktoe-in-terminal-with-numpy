from classes.game import Player
import numpy as np


def game(inp):
    player1 = Player("Bigya", "O", inp)
    player2 = Player("Binisha", "X", inp)
    players = [player1, player2]
    running = True
    while running:
        for player in players:
            player.get_input()

            def get_location():
                available_locations = player.choose_location()
                if len(available_locations) == 0:
                    print("\n!____Game Over____ !")
                    get_input = input("Enter N for New-game or E to Exit : ").upper()
                    if get_input == "E":
                        exit()
                    else:
                        new_locations = {
                                7: " ", 8: " ", 9: " ", 4: " ", 5: " ", 6: " ", 1: " ", 2: " ", 3: " "
                                    }
                        game(new_locations)
                try:
                    choice = int(input("\nEnter your choice: "))
                    if choice in available_locations:
                        index_of = available_locations.index(choice)
                        new_available_locations = available_locations.pop(index_of)
                        if str(choice) in str(new_available_locations):
                            player.choose_action(choice)
                            player.get_data(running)
                    else:
                        print("Action not possible")
                        get_location()
                except ValueError:
                    print("Action not possible")
                    get_location()
            get_location()
        pass


locations = {
    7: " ", 8: " ", 9: " ", 4: " ", 5: " ", 6: " ", 1: " ", 2: " ", 3: " "
}


game(locations)

