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
bridge = False
key = False
boss_key = False
torch_a = False
torch_b = False
torch_c = False
torch_d = False
seen_bridge = False
at_bridgeped = False
sword = False
shield = False
tunic = False
threekey = True
fourkey = True
fivekey = True
sixkey = True
tenkey = True

r_l = []
room = ["You are in a dimly lit room with a single door.", 1, None, None, None]
r_l.append(room)
room = ["You are in the compass room.", 11, 2, 0, 7]
r_l.append(room)
room = ["The only light comes from the room you just left.  There stands a lone pedestal, beyond which a ravine spans"
        " the width of the room.", None, None, None, 1]
r_l.append(room)
room = ["There is a pedestal in the center of the room, upon which rests a single key.  The Northern, Eastern, and "
        "Southern walls each bear a locked door.  The West door leads back to the bridge.", 4, 5, 6, 2]
r_l.append(room)
room = ["A steel shortsword rests on a pedestal.  Wooden bars protect a small key affixed to the north wall."
    , None, None, 3, None]
r_l.append(room)
room = ["This room is round, with flames roaring all around its perimeter.  At it's center, a red tunic rests on a\n"
        "pedestal, glimmering slightly in the firelight.  A key hangs beyond the flames on the East end of the room.",
        None, None, None, 3]
r_l.append(room)
room = ["A steel shield rests on a pedestal in the center of the room.  A key hangs on the Southern wall."
    , 3, None, None, None]
r_l.append(room)
room = ["This room contains an enemy slime.", None, 1, 8, None]
r_l.append(room)
room = ["This room contains an enemy giant spider.", 7, None, None, 9]
r_l.append(room)
room = ["This room contains an enemy skeleton.", 10, 8, None, None]
r_l.append(room)
room = ["A golden key with a ruby embedded in it's handle floats in the center of the room.", None, 7, 9, None]
r_l.append(room)
room = ["11", None, None, 1, None]
r_l.append(room)

current_room = 0                # unnecessary, but is technically true until after initial text
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
print("The set of doors at the far end of the room dwarfs the rest, seven men tall and nearly as wide.")
print("Set in the center of the doors is a massive blood-red gemstone, glittering in the torchlight.")
print("A large keyhole sits at around eye level.")
print()
input("[Press enter to continue]")

current_room = 1

while not done:
    print()
    print(r_l[current_room][0])
    print()

    if r_l[current_room] == r_l[3]:
        if threekey:
            print("You take the key.")
            key = True
            print()
            threekey = False
            r_l[3][0] = "The Northern, Eastern, and Southern doors each have locks.  The Western door leads back " \
                        "to the bridge room."

    elif r_l[current_room] == r_l[4] or r_l[current_room] == r_l[5] or r_l[current_room] == r_l[6]:
        if r_l[current_room] == r_l[4] and fourkey:     # loots sword room
            sword = True
            print("Using the sword you just obtained, you easily slice through the wooden bars and take the key.")
            print()
            fourkey = False
            r_l[4][0] = "You are in the sword room."
            key = True
        elif r_l[current_room] == r_l[5] and fivekey:   # loots tunic room
            tunic = True
            print("As soon as you don the tunic, the blazing heat of the flames subsides.  You feel as though you")
            print("can even touch the flames, and experience no harm.  So confident are you that you walk across the")
            print("room, reach through the wall of flame, and take the key from its hook.")
            print()
            fivekey = False
            r_l[5][0] = "You are in the tunic room."
            key = True
        elif r_l[current_room] == r_l[6] and sixkey:    # loots shield room
            shield = True
            print("You take up the shield, cross the room, and retrieve the key.")
            print()
            sixkey = False
            r_l[6][0] = "You are in the shield room."
            key = True

    elif r_l[current_room] == r_l[10] and tenkey:
        print("Stepping forward, you claim your prize.  This key is heavier than the others, with a certain weight")
        print("that speaks of a high quality and value.")
        tenkey = False
        boss_key = True

    print("Which direction would you like to move?")
    print()
    print("Options: [N] [E] [S] [W]")            # movement options
    if r_l[current_room] == r_l[2]:
        if not bridge:
            if not seen_bridge:
                r_l[2][0] = "You see a lone pedestal, beyond which a massive ravine spans the width of the room."
                seen_bridge = True
                print("Approach the pedestal [A]")
            else:
                if not bridge:
                    print("Approach the pedestal [A]")

    print()
    move = input("Input: ")                 # movement input
    print()

    if r_l[current_room] == r_l[2] and move.lower() == "a":                  # bridge puzzle
        at_bridgeped = True
        print("There are four buttons on the pedestal.")
        while at_bridgeped:
            if bridge:
                at_bridgeped = False
                continue
            print()
            print("[1] [2] [3] [4]")                # asks for a button
            press = int(input("Press a button: "))
            print()
            if press == 1:                          # puzzle magic
                if torch_a:
                    torch_a = False
                    print("The first torch flickers out.")
                else:
                    torch_a = True
                    print("The first torch roars to life.")
                if torch_b:
                    torch_b = False
                    print("The second torch flickers out.")
                else:
                    torch_b = True
                    print("The second torch roars to life.")
            elif press == 2:
                if torch_a:
                    torch_a = False
                    print("The first torch flickers out.")
                else:
                    torch_a = True
                    print("The first torch roars to life.")
                if torch_c:
                    torch_c = False
                    print("The third torch flickers out.")
                else:
                    torch_c = True
                    print("The third torch roars to life.")
            elif press == 3:
                if torch_b:
                    torch_b = False
                    print("The second torch flickers out.")
                else:
                    torch_b = True
                    print("The second torch roars to life.")
                if torch_c:
                    torch_c = False
                    print("The third torch flickers out.")
                else:
                    torch_c = True
                    print("The third torch roars to life.")
            elif press == 4:
                if torch_a:
                    torch_a = False
                    print("The first torch flickers out.")
                else:
                    torch_a = True
                    print("The first torch roars to life.")
                if torch_d:
                    torch_d = False
                    print("The fourth torch flickers out.")
                else:
                    torch_d = True
                    print("The fourth torch roars to life.")
            if torch_a and torch_b and torch_c and torch_d:
                bridge = True                                       # raises bridge
                print()
                print("The ground shakes as a bridge rises from the pit, forming a path to the other side.")
                r_l[2][0] = "You are in the bridge room."
                r_l[2][2] = 3

    elif move.lower() == "n" or move.lower() == "north":
        next_room = r_l[current_room][1]
        if next_room is None:
            print("You can't go that way.")
            print()
        elif r_l[next_room] == r_l[4] or r_l[next_room] == r_l[5] or r_l[next_room] == r_l[6] or r_l[next_room] == r_l[7]:          # checks for locked doors
            if r_l[next_room] == r_l[4]:
                if fourlock:                                                                # if door is locked
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        input("[Press enter to continue]")
                        print()
                        fourlock = False                # unlocks door
                        key = False                     # destroys key
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room            # moves to next room
            elif r_l[next_room] == r_l[5]:
                if fivelock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        input("[Press enter to continue]")
                        print()
                        fivelock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
            elif r_l[next_room] == r_l[6]:
                if sixlock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        input("[Press enter to continue]")
                        print()
                        sixlock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
            elif r_l[next_room] == r_l[7]:
                if sevenlock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        input("[Press enter to continue]")
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
        next_room = r_l[current_room][2]
        if next_room is None:
            print("You can't go that way.")
        elif r_l[next_room] == r_l[4] or r_l[next_room] == r_l[5] or r_l[next_room] == r_l[6] or r_l[next_room] == r_l[7]:          # checks for locked doors
            if r_l[next_room] == r_l[4]:
                if fourlock:                                                                # if door is locked
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        input("[Press enter to continue]")
                        print()
                        fourlock = False                # unlocks door
                        key = False                     # destroys key
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room            # moves to next room
            elif r_l[next_room] == r_l[5]:
                if fivelock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        input("[Press enter to continue]")
                        print()
                        fivelock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
            elif r_l[next_room] == r_l[6]:
                if sixlock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        input("[Press enter to continue]")
                        print()
                        sixlock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
            elif r_l[next_room] == r_l[7]:
                if sevenlock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        input("[Press enter to continue]")
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
        next_room = r_l[current_room][3]
        if next_room is None:
            print("You can't go that way.")
        elif r_l[next_room] == r_l[4] or r_l[next_room] == r_l[5] or r_l[next_room] == r_l[6] or r_l[next_room] == r_l[7]:          # checks for locked doors
            if r_l[next_room] == r_l[4]:
                if fourlock:                                                                # if door is locked
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        input("[Press enter to continue]")
                        print()
                        fourlock = False                # unlocks door
                        key = False                     # destroys key
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room            # moves to next room
            elif r_l[next_room] == r_l[5]:
                if fivelock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        input("[Press enter to continue]")
                        print()
                        fivelock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
            elif r_l[next_room] == r_l[6]:
                if sixlock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        input("[Press enter to continue]")
                        print()
                        sixlock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
            elif r_l[next_room] == r_l[7]:
                if sevenlock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        input("[Press enter to continue]")
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
        next_room = r_l[current_room][4]
        if next_room is None:
            print("You can't go that way.")
        elif r_l[next_room] == r_l[4] or r_l[next_room] == r_l[5] or r_l[next_room] == r_l[6] or r_l[next_room] == r_l[7]:
            if r_l[next_room] == r_l[4]:                                                              # checks for locked doors
                if fourlock:                                                                # if door is locked
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        input("[Press enter to continue]")
                        print()
                        fourlock = False                # unlocks door
                        key = False                     # destroys key
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room            # moves to next room
            elif r_l[next_room] == r_l[5]:
                if fivelock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        input("[Press enter to continue]")
                        print()
                        fivelock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
            elif r_l[next_room] == r_l[6]:
                if sixlock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        input("[Press enter to continue]")
                        print()
                        sixlock = False
                        key = False
                        current_room = next_room
                    else:
                        print("[Locked]")
                        print()
                else:
                    current_room = next_room
            elif r_l[next_room] == r_l[7]:
                if sevenlock:
                    if key:
                        print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
                        print("The key shatters into fragments of sparkling light, which shimmer for an instant")
                        print("before fading away.")
                        print()
                        input("[Press enter to continue]")
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
