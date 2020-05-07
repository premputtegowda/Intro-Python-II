import textwrap
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = [Item('jeans', 'denim jeans'), Item('shirt', 'short sleeve shirt')]
room['outside'].items = items
print(room['outside'].items[0].name)



# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']



#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input("Player name: "),room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = ['n','s','e','w']
valid_verbs = ['take', 'get', 'drop']

while True:
    print(player.current_room)
    print("======================")
    cmd = input(f"\n please enter the direction to move \nValid direction: {','.join(player.current_room.valid_directions())} to move or use verbs 'take' or 'get' to take an item, drop to return an item. Press 'q' to quit\n")
    print("======================")
   
    if cmd=='q':
        print("GoodBye")
        exit(0)
    elif cmd in directions:
            player.move(cmd)
    elif cmd.split(" ")[0] in valid_verbs:
        verb = cmd.split(" ")[0]
        item_name = cmd.split(" ")[1]
        if verb == 'take' or verb == 'get':
            print(player.on_take(item_name))
        elif verb == 'drop':
            print(player.on_drop(item_name))


    else:
        print("Invalid command")


