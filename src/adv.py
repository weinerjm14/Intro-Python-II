from room import Room
from player import Player

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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
action = "none"
oldroom = []
newplayer = Player("none", room["outside"])
print("Welcome adventurer. What is your name?")
newplayer.name = input("Enter Your Name:")
print(
    f"{newplayer.name}, you are  {newplayer.current_room}\n Please Choose A Direction"
)

direction = input("Pick a Direction: [s]outh [n]orth [e]ast [w]est e[x]it")
while not direction == "x":
    if direction == "n":
        newplayer.current_room = newplayer.current_room.n_to

    # elif direction == "s":
    #     newplayer.current_room.s_to = newplayer.current_room
    # elif direction == "e":
    #     newplayer.current_room.e_to = newplayer.current_room
    # elif direction == "w":
    #     newplayer.current_room.w_to = newplayer.current_room
    # else:
    #     print(f"{newplayer.name} please make select from the given choices \n")
    #     direction = input("Pick a Direction: [s]outh [n]orth [e]ast [w]est e[x]it")
    print(
        f"{newplayer.name} you have arrived at {newplayer.current_room}. \n please choose a direction\n"
    )
    # action == input(f"please choose [l]ook around or [m]ove to new room")
    # if action == "l":
    #     pass
    # if action == "m":
    #     direction = input("Pick a Direction: [s]outh [n]orth [e]ast [w]est e[x]it")
    direction = input("Pick a Direction: [s]outh [n]orth [e]ast [w]est e[x]it")

