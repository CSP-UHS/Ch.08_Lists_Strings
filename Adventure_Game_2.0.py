# import random
#
# class Player():
#     def __init__(self):
#         self.ac = 16
#         self.hp = 10
#         self.stats = ["Str", "Con", "Dex", "Wis", "Int", "Cha"]
#         self.weapon = "Fists"
#         self.shield = None
#         self.inventory = []
#
# def pseudopod():
#     attack = random.randint(1, 21) + 3
#     if attack >= Player.hp:
#         damage = (random.randint(1, 7) + 1) + random.randint(1, 7) + random.randint(1, 7)
# class Slime():
#     def __init__(self):
#         self.ac = 8
#         self.hp = 22
#         self.stats = [12, 6, 16, 1, 6, 2]
#         self.attack = [pseudopod()]


# def program():
#     global room_list, move, bridge, key, boss_key, current_room, next_room

room_list = []
room = ["You are in a dimly lit room with a single door.", 1, None, None, None, "[Unlocked]", "[Inactive]",
        "[Empty]"]
room_list.append(room)
room = ["You are in the compass room.", 11, 2, 0, 7, "[Unlocked]", "[Inactive]", "[Empty]"]
room_list.append(room)
room = ["The only light comes from the room you just left.  There stands a lone pedestal, beyond which a ravine "
        "spans the width of the room.", None, None, None, 1, "[Unlocked]", "[Inactive]", "[Empty]"]
room_list.append(room)
room = ["There is a pedestal in the center of the room, upon which rests a single key.  The northern, Eastern, and "
        "Southern walls each bear a locked door.  The West door leads back to the bridge.", 4, 5, 6, 2,
        "[Unlocked]", "[Inactive]", "[Loot]"]
room_list.append(room)
room = ["A steel shortsword rests on a pedestal.  Wooden bars protect a small key affixed to the north wall.", None,
        None, None, 3, "[Small lock]", "[Inactive]", "[Loot]"]
room_list.append(room)
room = ["This room is round, with flames roaring all around its perimeter.  At it's center, a red tunic rests on \n"
        "a pedestal, glimmering slightly in the firelight.  A key hangs beyond the flames on the East end of the"
        "room.", None, None, None, 3, "[Small lock]", "[Inactive]", "[Loot]"]
room_list.append(room)
room = ["A steel shield rests on a pedestal in the center of the room.  A key hangs on the southern wall.", 3, None,
        None, None, "[Small lock]", "[Inactive]", "[Loot]"]
room_list.append(room)
room = ["This room contains an enemy slime.", None, 1, 8, None, "[Small lock]", "[Active]", "[Empty]"]
room_list.append(room)
room = ["This room contains an enemy giant spider.", 7, None, None, 9, "[Unlocked]", "[Active]", "[Empty]"]
room_list.append(room)
room = ["This room contains an enemy skeleton.", 10, 8, None, None, "[Unlocked]", "[Active]", "[Empty]"]
room_list.append(room)
room = ["A golden key with a ruby embedded in it's handle floats in the center of the room.", None, 7, 9, None,
        "[Unlocked]", "[Inactive]", "[Loot]"]
room_list.append(room)
room = ["11", None, None, 1, None, "[Boss lock]", "[Active]", "[Empty]"]
room_list.append(room)

move = "undecided"

bridge = True
key = False
boss_key = False
current_room = 0
next_room = 1


def lock_check():
    global current_room, room_list, key, next_room, boss_key
    if room_list[next_room][5] == "[Small lock]":
        if key:
            print("You insert the key into the lock.  After a quarter turn, you hear an audible *click*")
            print("The key shatters into fragments of sparkling light, which shimmer for an instant")
            print("before fading away.")
            print()
            input("[Press enter to continue]")
            print()
            room_list[next_room][5] = "[Unlocked]"
            key = False
            current_room = next_room
        else:
            print("[Locked]")
            print()
    elif room_list[next_room][5] == "[Boss lock]":
        if boss_key:
            print(
                "You insert the golden key into it's lock.  The jewels on the key and door begin to glow in \n"
                "unison, brightening until the entire room is awash with bloodred light.")
            print()
            input("[Press enter to continue]")
            print()
            print("Suddenly, both gems shatter into countless crimson embers, which hang in the air for a moment")
            print("before fading away.")
            print()
            input("[Press enter to continue]")
            print()
            print(
                "You hear a deep echoing *thud*, and then a low rumbling as the doors slowly begin to swing inward.")
            print()
            room_list[next_room][5] = "[Unlocked]"
            boss_key = False
            current_room = next_room
        else:
            print("[Locked]")
            print()
    else:
        current_room = next_room


def choices():
    print("Options: [N] [E] [S] [W]")


def action():
    global current_room, bridge, move
    print("What would you like to do?")
    if current_room == 2 and bridge:
        print("Options: [N] North")
        print("         [E] East")
        print("         [S] South")
        print("         [W] West")
        print()
        move = input("Input: ")
        print()

    elif room_list[current_room][7] == "[Loot]":
        print("Options: [N] North")
        print("         [E] East")
        print("         [S] South")
        print("         [W] West")
        print("         [L] Loot")
        print()
        move = input("Input: ")
        print()

    elif room_list[current_room][6] == "[Active]":
        print("Options: [N] North")
        print("         [E] East")
        print("         [S] South")
        print("         [W] West")
        print()
        move = input("Input: ")
        print()

    elif current_room == 10:
        print("Options: [N] North")
        print("         [E] East")
        print("         [S] South")
        print("         [W] West")
        print()
        move = input("Input: ")
        print()

    elif current_room == 11:
        print("Options: [N] North")
        print("         [E] East")
        print("         [S] South")
        print("         [W] West")
        print()
        move = input("Input: ")
        print()
    else:
        print("Options: [N] North")
        print("         [E] East")
        print("         [S] South")
        print("         [W] West")
        print()
        move = input("Input: ")
        print()


def movement():
    global move, current_room, next_room

    if move.lower() == "n" or move.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room is None:
            print("You can't go that way.")
            print()
        else:
            lock_check()

    elif move.lower() == "e" or move.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room is None:
            print("You can't go that way.")
            print()
        else:
            lock_check()

    elif move.lower() == "s" or move.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room is None:
            print("You can't go that way.")
            print()
        else:
            lock_check()

    elif move.lower() == "w" or move.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room is None:
            print("You can't go that way.")
            print()
        else:
            lock_check()


def program():
    game = True

    print("You come to consciousness in a dimly lit room, enclosed by four walls of ancient stone brick.")
    print("Before you lies a single stone archway, leading into a dark room beyond.")
    print()
    input("[Press enter to stand up]")
    print()
    print("You slowly rise from the ground.")
    print()
    input("[Press enter to move forward]")
    print()
    print("You walk forward, through the doorway, and into the darkness beyond.")
    print()
    input("[Press enter to continue]")
    print()
    print(
        "As soon as you cross the threshold, blazing light fills the room as four torches come to life in its corners.")
    print("Unlike the previous room, this room has four doors, centered on each wall.")
    print("Behind you, the door through which you entered.")
    print("To your left, you see a wooden door with a large lock at its center.")
    print("There is a similar door opposite the first, though it bears a rusted ring of steel instead of a lock.")
    print(
        "The floor is made of smooth gray and shining black tiles, the latter of the two forming a massive compass rose,")
    print("each of its main points centered on a door.")
    print()
    input("[Press enter to continue]")

    current_room = 1

    while game:

        while current_room == 0:  # spawn
            print(room_list[current_room][0])
            print()
            action()
            movement()

        while current_room == 1:  # compass room
            print(room_list[current_room][0])
            print()
            action()
            movement()

        while current_room == 2:  # bridge room
            print(room_list[current_room][0])
            print()
            action()
            movement()

        while current_room == 3:  # armory
            print(room_list[current_room][0])
            print()
            action()
            movement()

        while current_room == 4:  # sword room
            print(room_list[current_room][0])
            print()
            action()
            movement()

        while current_room == 5:  # tunic room
            print(room_list[current_room][0])
            print()
            action()
            movement()

        while current_room == 6:  # shield room
            print(room_list[current_room][0])
            print()
            action()
            movement()

        while current_room == 7:  # slime room
            print(room_list[current_room][0])
            print()
            action()
            movement()

        while current_room == 8:  # spider room
            print(room_list[current_room][0])
            print()
            action()
            movement()

        while current_room == 9:  # skeleton room
            print(room_list[current_room][0])
            print()
            action()
            movement()

        while current_room == 10:  # boss key room
            print(room_list[current_room][0])
            print()
            action()
            movement()

        while current_room == 11:  # boss room
            print(room_list[current_room][0])
            print()
            action()
            movement()


if __name__ == "__main__":
    program()

