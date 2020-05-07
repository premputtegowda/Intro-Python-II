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

outside_room_items = [Item('jeans', 'denim jeans'), Item('shirt', 'short sleeve shirt'),Item('Cap', 'This is a baseball cap')]
outside_foyer_items = [Item('chair', 'This is a arm chair'), Item('couch', 'This is for indoor'),Item('table', 'This is a standing desk')]
room['outside'].items = outside_room_items
room['foyer'].items = outside_foyer_items




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
valid_verbs = ['take', 'get', 'drop','i', 'inventory']

while True:
    print(player.current_room)
    print("======================")
    cmd = input(f"\n Please pick an option from below \n 1. Enter  {','.join(player.current_room.valid_directions())} to move\n 2. Type 'take' or 'get' and the item name to take an item\n 3. Enter 'drop' and the item name to return an item.\n 4. Type 'i' or 'inventory' to see the inventory \n 4. Press 'q' to quit\n")
    print("======================")
   
    if cmd=='q':
        print("GoodBye")
        exit(0)
    elif cmd in directions:
            player.move(cmd)
    elif cmd.split(" ")[0] in valid_verbs:
        verb = cmd.split(" ")[0]
        
        if verb == 'take' or verb == 'get':
            item_name = cmd.split(" ")[1]
            print(player.on_take(item_name))
        elif verb == 'drop':
            item_name = cmd.split(" ")[1]
            print(player.on_drop(item_name))
        elif verb == 'i' or verb == 'i':
            for item in player.items:
                print(item.name)

    else:
        print("Invalid command")


