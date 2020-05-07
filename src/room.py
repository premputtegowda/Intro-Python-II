from player import Player
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items
# self.items[{name: 'pencil", description}, {name,description}]
    def __str__(self):
        return f"Room: {self.name}, Description:{self.description}"

    
    def valid_directions(self):
        movement = []
        if self.n_to is not None:
            movement.append('n')
        if self.s_to is not None:
            movement.append('s')
        if self.e_to is not None:
            movement.append('e')
        if self.w_to is not None:
            movement.append('w')
        return movement
