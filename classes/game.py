import numpy as np


class Player:
    def __init__(self, name, action, location):
        self.action = action
        self.location = location
        self.name = name

    def choose_location(self):
        print("Locations:")
        available_locations = []
        for j in self.location:
            if self.location[j] == ' ':
                print("->" + str(j), end='  ')
                available_locations.append(j)
        return available_locations

    def choose_action(self, choice):
        # if choice in self.location:
        self.location[choice] = self.action
        return self.location

    def get_data(self, running):
        keys = []
        for key in self.location:
            keys.append(self.location[key])
        x = np.array(keys).reshape(3, 3)
        conditions = [np.array(x.diagonal()), np.fliplr(x).diagonal()]
        for i in range(3):
            conditions.append(x[:, i])
            conditions.append(x[i, :])
        conditions = np.array(conditions)
        # print(conditions)
        win = np.array([self.action, self.action, self.action])
        for i in range(len(conditions)):
            if np.all(conditions[i] == win):
                print(f"---Game Over---\nPlayer {self.name} Wins!")
                Player.get_input(self)
                running = False
                exit()

    def get_input(self):
        print("\nPLAYER", self.name, "\n")
        print(f"     {self.location[7]} | {self.location[8]} | {self.location[9]}     ")
        print("    ------------")
        print(f"     {self.location[4]} | {self.location[5]} | {self.location[6]}     ")
        print("    ------------")
        print(f"     {self.location[1]} | {self.location[2]} | {self.location[3]}    ")
