'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''

fourlock = True
fivelock = True
sixlock = True
sevenlock = True
elevenlock = True
key = False

room_list = []
room = ["0", 1, None, None, None]
room_list.append(room)
room = ["1", 11, 2, 0, 7]
room_list.append(room)
room = ["2", None, 3, None, 1]
room_list.append(room)
room = ["3", 4, 5, 6, 2]
room_list.append(room)
room = ["4", None, None, 3, None]
room_list.append(room)
room = ["5", None, None, None, 3]
room_list.append(room)
room = ["6", 3, None, None, None]
room_list.append(room)
room = ["7", None, 1, 8, None]
room_list.append(room)
room = ["8", 7, None, None, 9]
room_list.append(room)
room = ["9", 10, 8, None, None]
room_list.append(room)
room = ["10", None, 7, 9, None]
room_list.append(room)
room = ["11", None, None, 1, None]
room_list.append(room)

current_room = 0
done = False

print("You come to consciousness in a dimly lit room, enclosed by four walls of ancient stone brick.")
print("Before you lies a single stone archway, leading into a dark room beyond.")
print()
input("[Press enter to stand up]")
print()
print("you slowly rise from the ground.")
print()
input("[Press enter to move forward]")
print()
print("You walk forward, through the doorway, and into the darkness beyond.")
print()
input("[Press enter to continue]")
print()
print("As soon as you cross the threshhold, blazing light fills the room as four torches come to life in its corners.")
print("Unlike the previous room, this room has four doors, centered on each wall.")
print("Behind you, the door through which you entered.")
print("To your left, you see a wooden door with a large lock at its center.")
print("There is a similar door opposite the first, though it bears a rusted ring of steel instead of a lock.")
print("The floor is made of smooth gray and shining black tiles, the latter of the two forming a massive compass rose,")
print("each of its main points centered on a door.")
print()
input("[Press enter to continue]")
print()
print("The set of doors at the far end of the room dwarfs the rest, seven men tall and nearly just as wide.")
print("Set in the center of the doors is a massive blood-red gemstone, glittering in the torchlight.")
print("A large keyhole sits at around eye level.")
print()
input("[Press enter to continue]")

while not done:
    print()
    print(room_list[current_room][0])
    print()
    print("Which direction would you like to move?")
    print()
    print("Options: N, E, S, W")            # movement options
    print()
    move = input("Input: ")                 # movement input
    print()

    if move.lower() == "n" or move.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room is None:
            print("You can't go that way.")
            print()
        elif next_room == 4 or next_room == 5 or next_room == 6 or next_room == 7:          # checks for locked doors
            if next_room == 4:
                if fourlock:                                                                # if door is locked
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        fourlock = False                # unlocks door
                        key = False                     # destroys key
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room            # moves to next room
            elif next_room == 5:
                if fivelock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        fivelock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
            elif next_room == 6:
                if sixlock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        sixlock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
            elif next_room == 7:
                if sevenlock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        sevenlock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
        else:
            current_room = next_room

    elif move.lower() == "e" or move.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room is None:
            print("You can't go that way.")
        elif next_room == 4 or next_room == 5 or next_room == 6 or next_room == 7:          # checks for locked doors
            if next_room == 4:
                if fourlock:                                                                # if door is locked
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        fourlock = False                # unlocks door
                        key = False                     # destroys key
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room            # moves to next room
            elif next_room == 5:
                if fivelock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        fivelock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
            elif next_room == 6:
                if sixlock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        sixlock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
            elif next_room == 7:
                if sevenlock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        sevenlock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
        else:
            current_room = next_room

    elif move.lower() == "s" or move.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room is None:
            print("You can't go that way.")
        elif next_room == 4 or next_room == 5 or next_room == 6 or next_room == 7:          # checks for locked doors
            if next_room == 4:
                if fourlock:                                                                # if door is locked
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        fourlock = False                # unlocks door
                        key = False                     # destroys key
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room            # moves to next room
            elif next_room == 5:
                if fivelock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        fivelock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
            elif next_room == 6:
                if sixlock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        sixlock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
            elif next_room == 7:
                if sevenlock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        sevenlock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
        else:
            current_room = next_room

    elif move.lower() == "w" or move.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room is None:
            print("You can't go that way.")
        elif next_room == 4 or next_room == 5 or next_room == 6 or next_room == 7:          # checks for locked doors
            if next_room == 4:
                if fourlock:                                                                # if door is locked
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        fourlock = False                # unlocks door
                        key = False                     # destroys key
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room            # moves to next room
            elif next_room == 5:
                if fivelock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        fivelock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
            elif next_room == 6:
                if sixlock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        sixlock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
            elif next_room == 7:
                if sevenlock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        sevenlock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
        else:
            current_room = next_room

    elif move.lower() == "q" or move.lower() == "quit":
        done = True

    else:
        print("I'm sorry, I don't quite understand what you want to do.  Could you try again?")
