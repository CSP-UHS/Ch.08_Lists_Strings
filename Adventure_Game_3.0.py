import random
"""
-----room descriptions-----
"""
# r0 = "spawn"
# r1 = "compass room"
# r2 = "bridge room"
# r3 = "armoury"
# r4 = "fighter room"
# r5 = "mage room"
# r6 = "archer room"
# r7 = "slime room"
# r8 = "spider room"
# r9 = "skeleton room"
# r10 = "boss key room"
# r11 = "boss room"
r0 = "You are standing in a cold, dark room.  The only exit is a stone archway before you."
r1 = "Stepping into the room, four braziers, one in each corner of the room, roar to life.\nAcross the floor spans a " \
     "massive compass rose, laid in shining black tile.\n" \
     "To the west, there is a stone door bound in chains, which sparkle with blue light.\n" \
     "To the east, an open archway leads to a dimly lit room.\n" \
     "And before you, a magnificent set of double doors, made of of gold and steel.\n" \
     "They stand 25 feet tall and nearly as wide, with a large ruby set at their seam, 5 feet off the ground.\n" \
     "At its center, there is a keyhole."
r2 = "A deep ravine spans the center of the room, running from north to south.\n" \
     "In front of you stands a pedestal with four buttons made of smooth black stone.\n" \
     "Across the room, you see an archway, above which hang four unlit torches.\n"
r3 = "There are three doors in this room, in addition to the one you just entered from.\n" \
     "first, to the north.  A heavy steel door, above which is carved a crest with sword and shield.\n" \
     "To the south, a rough log door, similar to that of a hunting cabin.  Carved above it is a quiver and bow.\n" \
     "Finally, to the west lies a finely made dark mahogany door. Its symbol is a book and quill.\n" \
     "In the center of the room, a small plaque reads: \n" \
     "\"Three paths before you, all may be explored, only one shall you travel.\""
r4 = "Banners hang from the walls of this room, ancient suits of armor standing watch.\n" \
     "You are drawn to the shining sword and shield, hanging from the wall."
r5 = "Every wall is covered in book cases, filled to bursting with endless tomes.\n" \
     "In the center of the room lies a pedestal made of black marble, atop which rests a crystal crackling with\n" \
     "blue energy."
r6 = "The walls of this room are adorned with dozens of trophies from coutless hunts.\n" \
     "Mounted on the far wall is a sleek wooden bow, and a quiver full of arrows."
r7 = "This damp room seems to excrete ooze from its walls.\n" \
     "To the south is a door, and before you, a gelatinous lump slithering toward you."
r8 = "The walls are covered in webs, nearly entirely obscuring a door to the west.\n" \
     "A massive jet black arachnid skitters toward you on its long, spindly legs."
r9 = "This room was once a crypt, its floor now littered with bones and dust.  The next room is to the north.\n" \
     "One set of bones rises to defend its slumbering brethren, rushing at you with longsword in hand."
r10 = "A large golden key floats in the center of this room.  To the east, what first appears to be a large\n" \
      "mirror reflects the great doors of the compass room, instead of your reflection.  You feel as though you\n" \
      "could walk right through its dully shimmereing surface."
r11 = "Upon inserting the key into the lock on the massive doors, the large ruby begins to glow with red light.\n" \
      "brighter and brighter it grows, until both it and the key shatter into countless fragments of light, which\n" \
      "freeze midway through the air, briefly glittering before fading away.\n" \
      "The doors rumble, then swing inward.  As you enter, you find yourself facing a great black wyrm.\n" \
      "Its deep growl resonates throughout the chamber.  It is ready to meet your challenge.\n"
"""
-----room contents-----
"""
# [description, north, east, south, west, locked, looted, enemies, puzzle, message]
rl = []
room = [r0, 1, None, None, None, "unlocked", "empty", "clear", "clear", None]
rl.append(room)
room = [r1, None, 2, 0, None, "unlocked", "empty", "clear", "clear", None]
rl.append(room)
room = [r2, None, None, None, 1, "unlocked", "empty", "clear", "active", None]
rl.append(room)
room = [r3, 4, 5, 6, 2, "unlocked", "empty", "clear", "clear", None]
rl.append(room)
room = [r4, None, None, 3, None, "unlocked", "items", "clear", "clear", None]
rl.append(room)
room = [r5, None, None, None, 3, "unlocked", "items", "clear", "clear", None]
rl.append(room)
room = [r6, 3, None, None, None, "unlocked", "items", "clear", "clear", None]
rl.append(room)
room = [r7, None, 1, 8, None, "locked", "empty", "slime", "clear", None]
rl.append(room)
room = [r8, 7, None, None, 9, "locked", "empty", "spider", "clear", None]
rl.append(room)
room = [r9, 10, 8, None, None, "locked", "empty", "skeleton", "clear", None]
rl.append(room)
room = [r10, None, 1, 9, None, "locked", "items", "clear", "clear", None]
rl.append(room)
room = [r11, None, None, 1, None, "boss_lock", "empty", "dragon", "clear", None]
rl.append(room)

"""
-----variable definitions-----
"""

game = True
cr = 0
combat = False

"""
-----command definitions-----
"""


def move():             # player inputs an option, carries out if possible
    global cr
    print("What would you like to do?\n")
    print("[N] North\n[E] East\n[S] South\n[W] West")
    if rl[cr][6] == "items" or rl[cr][8] == "active":
        print("[I] Interact")
    print()
    choice = input("Input: ")
    print()

    clist = ["i", "n", "e", "s", "w", "north", "east", "south", "west"]
    movecheck = 0                                                   # This freaking genius is but a sample of my power.
    for i in range(len(clist)):                                     # It handles movement without me having to retype
        if choice.lower() == clist[i]:                              # a statement for each direction.
            if i == 0:                                              # I'm the best.
                interact()
                break
            elif i <= 4:
                nr = rl[cr][i]
            else:
                nr = rl[cr][i - 4]
            if nr is None:
                print("You can't go that way.")
                print()
            else:
                cr = nr
            break
        else:
            movecheck += 1
    if movecheck == 8:
        print("Invalid command")
        print()


def puzzle():           # puzzle obstacle
    global bridge
    at_bridgeped = True
    bridge = False
    torch_a = False
    torch_b = False
    torch_c = False
    torch_d = False
    print("There are four buttons on the pedestal.")
    while at_bridgeped:
        if bridge:
            at_bridgeped = False
            continue
        print()
        print("[1] [2] [3] [4]")  # asks for a button
        press = int(input("Press a button: "))
        print()
        if press == 1:  # puzzle magic
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
        else:
            print("[invalid command]")
        if torch_a and torch_b and torch_c and torch_d:
            bridge = True  # raises bridge
            print()
            print("The ground shakes as a bridge rises from the pit, forming a path to the other side.")
            print()
            rl[2][8] = "clear"
            rl[2][2] = 3


def interact():         # interacts with/picks up any items or devices in a room
    global cr, playerClass
    if rl[cr][6] == "items":
        rl[cr][6] = "looted"
        if rl[cr] == rl[4] or rl[cr] == rl[5] or rl[cr] == rl[6]:
            if rl[4][6] == "looted" or rl[5][6] == "looted" or rl[6][6] == "looted":
                if rl[cr] == rl[4]:
                    print("Taking up the sword and shield, you feel a sense of confidence wash over you.")
                    playerClass = "fighter"
                    print()
                    input("[press enter to leave room]")
                    print()
                    print("Stepping back into the armoury, you notice the eastern and southern doors have vanished.")
                    print("As you look over your shoulder, you see the room you just left has disappeared as well.")
                    print()
                    input("[press enter to continue]")
                    print()
                elif rl[cr] == rl[5]:
                    print("Picking up the crystal, you feel its power surge through your body.")
                    playerClass = "wizard"
                    print()
                    input("[press enter to leave room]")
                    print()
                    print("Stepping back into the armoury, you notice the northern and southern doors have vanished.")
                    print("As you look over your shoulder, you see the room you just left has disappeared as well.")
                    print()
                    input("[press enter to continue]")
                    print()
                else:
                    print("You sling the quiver over your shoulder, and take up the bow.")
                    print("They fill you with a sense of calm.")
                    playerClass = "ranger"
                    print()
                    input("[press enter to leave room]")
                    print()
                    print("Stepping back into the armoury, you notice the northern and eastern doors have vanished.")
                    print("As you look over your shoulder, you see the room you just left has disappeared as well.")
                    print()
                    input("[press enter to continue]")
                    print()
                print("You hear a loud *thud* and feel a wave of magical energy.\n"
                      "Somehow, you know the chained door is now open.")
                print()
                cr = 3
                rl[3][1] = None
                rl[3][2] = None
                rl[3][3] = None
                rl[1][4] = 7
        elif rl[cr] == rl[10]:
            print("You take the key.")
            print()
            rl[1][1] = 11
    elif rl[cr] == rl[2]:
        puzzle()


"""
-----combat data-----
"""


def roll(dice, sides):
    total = 0
    for i in range(1, dice + 1):
        result = random.randint(1, sides)
        total += result
    return total


# -- Player --
plvl = 1
playerAtkMod = plvl * 2 + 2
playerDmgMod = plvl * 2
playerAC = 10 + 2 * plvl

# -- Slime --
slimeHP = 12
slimeAC = 8
slimeAtkMod = 3


def slime_atk():

    dmg = roll(1, 6) + 1 + roll(1, 4)

    return dmg


# -- Spider --
spiderHP = 24
spiderAC = 14
spiderAtkMod = 5

# -- Skeleton --
skeletonHP = 36
skeletonAC = 13
skeletonAtkMod = 4

# -- Dragon --
dragonHP = 75
dragonAC = 15
dragonAtkMod = 6


"""
-----main-----
"""


def main():
    global game, plvl, cr
    while game:
        print(rl[cr][0])
        print()
        if rl[cr] == rl[0]:
            rl[cr][0] = "[spawn]"
        elif rl[cr] == rl[1]:
            rl[cr][0] = "[compass room]"
        elif rl[cr] == rl[2]:
            rl[cr][0] = "[bridge room]"
        elif rl[cr] == rl[3]:
            rl[cr][0] = "[armoury]"
        elif rl[cr] == rl[4]:
            rl[cr][0] = "[sword room]"
        elif rl[cr] == rl[5]:
            rl[cr][0] = "[crystal room]"
        elif rl[cr] == rl[6]:
            rl[cr][0] = "[bow room]"
        elif rl[cr] == rl[7]:
            rl[cr][0] = "[slime room]"
        elif rl[cr] == rl[8]:
            rl[cr][0] = "[spider room]"
        elif rl[cr] == rl[9]:
            rl[cr][0] = "[skeleton room]"
        elif rl[cr] == rl[10]:
            rl[cr][0] = "[boss key room]"
        elif rl[cr] == rl[11]:
            rl[cr][0] = "You go forth, ready to face the dragon again."
        move()
        if rl[cr] == rl[7] and rl[cr][0] != "[slime room]":
            print(rl[cr][0])
        elif rl[cr] == rl[8] and rl[cr][0] != "[spider room]":
            print(rl[cr][0])
        elif rl[cr] == rl[9] and rl[cr][0] != "[skeleton room]":
            print(rl[cr][0])
        elif rl[cr] == rl[11]:
            print(rl[cr][0])
            rl[cr][0] = "You go forth, ready to face the dragon again."
        if rl[cr][7] == "clear":
            combat = False
        else:
            combat = True
            playerHP = 12 * plvl
            print("An enemy", rl[cr][7], "stands before you!")
            print()
            if rl[cr][7] == "slime":
                enemyHP = slimeHP
                enemyAC = slimeAC
                enemyAtkMod = slimeAtkMod
            elif rl[cr][7] == "spider":
                enemyHP = spiderHP
                enemyAC = spiderAC
                enemyAtkMod = spiderAtkMod
            elif rl[cr][7] == "skeleton":
                enemyHP = skeletonHP
                enemyAC = skeletonAC
                enemyAtkMod = skeletonAtkMod
            elif rl[cr][7] == "dragon":
                enemyHP = dragonHP
                enemyAC = dragonAC
                enemyAtkMod = dragonAtkMod
        while combat:
            print("player HP:", playerHP)
            print(rl[cr][7], "HP:", enemyHP)
            print()
            print("What would you like to do?")
            print()
            print("[A] Attack")
            print("[R] Run away")
            print()
            choice = input("Input: ")
            print()
            if choice.lower() == "r" or choice.lower() == "run away":
                cr = 1
                combat = False
                print("You fled to the safety of the compass room!")
                print()
                break
            atk = roll(1, 20)
            if atk == 20:
                pcrit = True
            else:
                pcrit = False
            atk += playerAtkMod
            if atk >= enemyAC:
                playerDmg = roll(plvl, 8)
                if pcrit:
                    playerDmg *= 2
                    print("Natural 20!")
                playerDmg += playerDmgMod
                enemyHP -= playerDmg
                if playerClass == "fighter":
                    print("Your sword slashes into your foe.")
                    print(playerDmg, "slashing damage!")
                    print()
                elif playerClass == "ranger":
                    print("Your arrow finds its mark.")
                    print(playerDmg, "piercing damage!")
                    print()
                elif playerClass == "wizard":
                    print("You fire a bolt of magical energy, which slams into your foe.")
                    print(playerDmg, "lightning damage!")
                    print()
                else:
                    print("Woah,", playerDmg, "damage!  What'd you even hit it with?!")
                    print()
                if enemyHP <= 0:
                    print("You defeated the", rl[cr][7] + "!")
                    print()
                    if rl[cr][7] == "slime":
                        rl[cr][0] = "[slime room]"
                        print("You feel refreshed, and a bit stronger than before.")
                        print()
                    elif rl[cr][7] == "spider":
                        rl[cr][0] = "[spider room]"
                        print("You feel refreshed, and a bit stronger than before.")
                        print()
                    elif rl[cr][7] == "skeleton":
                        rl[cr][0] = "[skeleton room]"
                        print("You feel refreshed, and a bit stronger than before.")
                        print()
                    elif rl[cr][7] == "dragon":
                        print("The great dragon falls to the ground, crumbling into a pile of dust.")
                        print("On the opposite end of the room, a section of the wall sparkles, before fading away,")
                        print("revealing a staircase leading to freedom beyond.")
                        print()
                        print("[GAME COMPLETE]")
                        game = False
                        break
                    rl[cr][7] = "clear"
                    plvl += 1
                    combat = False
                    break
            else:
                print("Your attack missed!")
                print()

            enatk = roll(1, 20)
            if enatk == 20:
                ecrit = True
            else:
                ecrit = False
            enatk += enemyAtkMod
            if enatk >= playerAC:
                if rl[cr][7] == "slime":
                    enemyDmg = roll(1, 6)
                elif rl[cr][7] == "spider":
                    enemyDmg = roll(2, 6)
                elif rl[cr][7] == "skeleton":
                    enemyDmg = roll(3, 6)
                else:
                    enemyDmg = roll(2, 10)
                if ecrit:
                    enemyDmg *= 2
                    print("Natural 20!")
                playerHP -= enemyDmg
                if rl[cr][7] == "slime":
                    print("You took", enemyDmg, "acid damage!")
                    print()
                elif rl[cr][7] == "spider":
                    print("You took", enemyDmg, "venom damage!")
                    print()
                elif rl[cr][7] == "skeleton":
                    print("You took", enemyDmg, "slashing damage!")
                    print()
                else:
                    print("You took", enemyDmg, "fire damage!")
                    print()
                if playerHP <= 0:
                    combat = False
                    game = False
                    print("You died!")
                    print()
                    print("[GAME OVER]")
                    print()
                    break
            else:
                print("The enemy", rl[cr][7] + "'s attack missed!")
                print()


"""
-----program executor----- DONE
"""
if __name__ == "__main__":
    main()
