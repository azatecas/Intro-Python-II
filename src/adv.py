from room import Room
from player import Player
from item import Item
import textwrap
import msvcrt

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


items = {
    "rock": Item("Rock","object that does damage"),
    "stick": Item("Stick","wooden Stick"),
    "computer": Item("Computer"," a powerful computer for playing games"),
    "socks": Item("Socks", "clothing item to put on your feet"),
    "table": Item("Table", "wooden furniture" ),
    "chess": Item("chess","chess board game"),
    "baseball": Item("baseball","a sports ball for the sport of baseball")
}
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to room
room['outside'].items = [items["rock"], items["stick"]]
room['foyer'].items = [items['computer'], items['table']]
room['overlook'].items = [items["socks"], items["socks"]]
room['narrow'].items = [items["chess"]]
room['treasure'].items = [items["baseball"]]

# Main

#wrapper
wrapper = textwrap.TextWrapper(width=50)



# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
def action(command, player):
    command_list = command.split(" ")
    if "get" in command_list and len(command_list) <= 2:
        if command_list[1] in [item.name.lower() for item in player.current_room.items]:
            player.inventory.append(items[command_list[1].lower()])
            player.current_room.items.remove(items[command_list[1].lower()])
            print(f"You added {command_list[1]} to inventory")

        else:
            print("Item is not available in this room")

    elif "drop" in command_list and len(command_list) < 2:
        if command_list[1] in [item.name.lower() for item in player.inventory]:
            player.inventory.remove(items[command_list[1].lower()])
            player.current_room.items.append(items[command_list[1].lower()])
            print(f"You dropped {command_list[1]}")
        else:
            print("item not in inventory")
    elif command == "nothing":
        pass
    elif command == "q":
        quit()

    else:
        print("Command not valid")
        
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def room_exists(player, user_input):
    direction = {"n":player.current_room.n_to, "s":player.current_room.s_to, "w":player.current_room.w_to, "e":player.current_room.e_to}

    if user_input == "q":
        exit()
    
    if direction[user_input] != None:
        player.current_room = direction[user_input]

        #print room
        print(f"Current Room: {player.current_room.name}")

        #print description
        word_list = wrapper.wrap(text=player.current_room.description)
        for elem in word_list:
            print(elem)

        print("Items available: ")
        for item in player.current_room.items:
            print(f"{item.name}")

        command_input = input("what to do with items?")
        action(command_input, player)

    else:
        print("no room in that direction")



# Make a new player object that is currently in the 'outside' room.
new_player = Player("luis", room["outside"])
# Write a loop that:

while True:
    user_input = msvcrt.getwch().lower()
    valid_inputs = ["n","s","e","w",]

    if user_input in valid_inputs:
        room_exists(new_player, user_input)
        continue
    else:
        print("use n, w, s, e, to move")