'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import random

lock = None

room_list = []
#create rooms and add to room list
room = ["You are in the master bedroom. There are two dressers to your left and right. (N,E,S,W,i,b)", 2, 3, 4, 1] #North #East #South #West
room_list.append(room)

room = ["You are in the closet. (E,i,b)", None, 0, None, None]
room_list.append(room)

room = ["You are in the master bathroom (S,i,b)", None, None, 0, None]
room_list.append(room)

room = ["You are in the kitchen hallway (N,E,S,W,i,b)", 5, lock, 6, 0]
room_list.append(room)

room = ["You are in the livingroom hallway (N,S,i,b)", 0, None, 7, None]
room_list.append(room)

room = ["You are in the Guest bedroom (S,i,b)", None, None, 3, None]
room_list.append(room)

room = ["You are in the Hallway bathroom (N,i,b)", 3, None, None, None]
room_list.append(room)

room = ["You are in the Living room (N,E,i,b)", 4, 9, None, None]
room_list.append(room)

room = ["You are in the Kitchen (W,i,b)", None, None, None, 3]
room_list.append(room)

room = ["You are in the Living room Bathroom (W,i,b)", None, None, None, 7]
room_list.append(room)

done = False

while not done:

    code = random.randint(1000,10000)
    current_room = 0
    chainsaw = False
    gun = False
    key = False
    flamethrower = False
    invest = ""

    backpack = []

    while not done:
        print()
        print(room_list[current_room][0])
        bing = input("")

        # North
        if bing.upper() == "N" or bing.upper() == "NORTH":
            next_room = room_list[current_room][1]
            if next_room == None:
                print("You can't go that way!")
            else:
                current_room = next_room

        # East
        elif bing.upper() == "E" or bing.upper() == "EAST":
            next_room = room_list[current_room][2]
            if next_room == None:
                print("You can't go that way!")
            else:
                current_room = next_room

        # South
        elif bing.upper() == "S" or bing.upper() == "SOUTH":
            next_room = room_list[current_room][3]
            if next_room == None:
                print("You can't go that way!")
            else:
                current_room = next_room

        # West
        elif bing.upper() == "W" or bing.upper() == "WEST":
            next_room = room_list[current_room][4]
            if next_room == None:
                print("You can't go that way!")
            else:
                current_room = next_room
        # QUIT
        elif bing.lower() == "q" or bing.lower() == "quit":
            done = True

        # INVESTIGATE
        elif bing.lower() == "i" or bing.lower() == "investigate":
            print()

        # BACKPACK
        elif bing.lower() == "b" or bing.lower() == "backpack":
            print(backpack)

        # STUPID
        else:
            print("Not sure you understand the game pal.")

        if current_room == 0: #Master Bedroom
            if bing.lower() == "i" or bing.lower() == "investigate":
                invest = input("Left or Right dresser? ")
                if invest.lower() == "l" or invest.lower() == "left":
                    print("You found a Glock 19 with 10 rounds in it, you added the gun to your inventory.")
                    pack = ["gun"]
                    backpack.append(pack)
                    gun = True
                    pass
                elif invest.lower() == "r" or invest.lower() == "right":
                    if gun == False:
                        print("You trip and fall into the open dresser,")
                        print("All of a sudden you see a bright light and a large expanse of grassland that you have fallen into.")
                        print("You have found Narnia!")
                        print("A large yellow shape starts to approach you...")
                        print("It's Azland!")
                        print("As soon as he is within 10 feet of you, Azland pounces and rips off your head.")
                        print("You died, but at least you died in peace...")
                        break
                    else:
                        print("You trip and fall into the open dresser,")
                        print("All of a sudden you see a bright light and a large expase of grassland that you have fallen into.")
                        print("You have found Narnia!")
                        print("A large yellow shape starts to approach you...")
                        print("It's Azland!")
                        print("As Azland approaches he seems to become more hostile towards you.")
                        print("When he reaches 10 meters away from you he tries to pounce on you.")
                        print("You whip your Glock out of your pocket and fire 10 rounds into his head and chest.")
                        print("You survived and killed Azland.")
                        print("You live the rest of your days in depression and self-loathing running from the beings of Narnia.")
                        break
                else:
                    print("You avoid both dressers and are still in the master bedroom.")

            else:
                pass

        elif current_room == 1: #closet
            if bing.lower() == "i" or bing.lower() == "investigate":
                invest = input("There is a shelf above your head, do you want to interact with it? ")
                if invest.lower() == "y" or invest.lower() == "yes":
                    bing = input("You find a combination locked safe on the shelf... Do you attempt to unlock it? ")
                    if bing.lower() == "y" or bing.lower() == "yes":
                        safe = int(input("What is the code: "))
                        if safe == code:
                            print("You successfully opened the safe, you found a chainsaw")
                            pack = ["chainsaw"]
                            backpack.append(pack)
                            chainsaw = True

                        else:
                            print("You attempted the code and got it wrong.")
                            print("The door behind you seals up and gas spreads through the room...")
                            print("You died to toxic gas.")
                            break
                    else:
                        print("You decide to try and find the code.")
                else:
                    print("You decide to explore the other rooms before you attempt this one.")
            else:
                pass

        elif current_room == 2: #master bathroom
            if bing.lower() == "investigate" or bing.lower() == "i":
                invest = input("There is a medicine cabinet, would you like to investigate it? ")
                if invest.lower() == "y" or invest.lower() == "yes":
                    if key == False:
                        print("The cabinet is locked. You need a key")
                    else:
                        bing = input("There is melatonin on the shelf, do you take it? ")
                        if bing.lower() == "y" or bing.lower() == "yes":
                            print("You took three weeks worth of melatonin in one sitting.")
                            print("You start to feel woozy...")
                            print("You pass out onto the floor, the world going dark in front of your eyes...")
                            break
                        else:
                            print("You decide to leave the melatonin and explore the other rooms.")
                else:
                    print("You decide to explore the other rooms first.")
            else:
                pass

        elif current_room == 3: #kitchen hallway
            if bing.lower() == "investigate" or bing.lower() == "i":
                invest = input("There is a keypad near the end of the hallway, \nwould you like to approach it? ")
                if invest.lower() == "y" or invest.lower() == "yes":
                    print("The keypad has a four digit code lock...")
                    bing = input("Would you like to attempt the code? ")
                    if bing.lower() == "yes" or bing.lower() == "y":
                        safe = int(input("Code: "))
                        if safe == code:
                            print("The kitchen door has been unlocked.")
                            current_room = 8
                        else:
                            print("All of a sudden you hear a shuddering sound...")
                            print("You spin around to see the far wall of the hallway shudder into motion...")
                            print("The walls are compressing uppon you!")
                            print("HELP US 3PO!!")
                            print("The wall slowly crushes you into a thin line of spilled blood on the wall.")
                            print("No one is around to hear your screams of agony.")
                            break
                    else:
                        print("You decide to try and find the code in another room before you attempt.")
                else:
                    print("You decide to explore the rest of the house first.")
            else:
                pass

        elif current_room == 4: #living room hallway
            if bing.lower() == "investigate" or bing.lower() == "i":
                print("As you pass through the hallway something strange starts to happen...")
                print("As you continue, the room starts to disolve into ones and zeros...")
                print("You start to see a figure take shape in the wall to your left...")
                print("A white wrinkly hand shoots out of the wall and attaches itself to the back of your neck!")
                print("You peer fearfully at the wall as a face presses itself uppon it...")
                print("A very old looking white-haired Keanu Reeves with pitch-black sunglasses peers back at you.")
                print("'Mission...'")
                print("'Accomplished...'")
                print("He slowly states as he lifts your spine straight out of your back and through your neck...")
                print("You have been slain by the great John Wick.")
                break
            else:
                pass

        elif current_room == 5: #guest bedroom
            if bing.lower() == "investigate" or bing.lower() == "i":
                print("In the room there is a bed smack-dab in the middle with armuoirs to your left and right.")
                print("There is a note on the bed...")
                print("It reads")
                print(code)
            else:
                pass

        elif current_room == 6: #hallway bathroom
            if bing.lower() == "investigate" or bing.lower() == "i":
                print("You spot a weird looking skeleton on the toilet in the corner...")
                print("It seems to have a weird sweeping white haircut and a strange sequined jacket.")
                print("All of a sudden, the roof starts to emit a sound...")
                print("'But I... Can't help.... Falling in love... With... You...")
                print("As the song plays, the skeleton rises from the toilet and stumbles towards you...")
                print("You rush to the door!")
                print("But it's locked.")
                print("The skeleton reaches inside it's chest and pulls out one of it's ribs.")
                print("You scream.")
                print("The screams continue, as the skeletal Elvis proceeds to viciously stab you to death with his rib.")
                break
            else:
                pass

        elif current_room == 7: #living room
            if bing.lower() == "investigate" or bing.lower() == "i":
                print("There is a large ornate wooden door blocking your escape to the front yard.")
                invest = input("Would you like to attempt escape?")
                if invest.lower() == "yes" or invest.lower() == "y":
                    bing = input("What would you like to use against the door? ")
                    if flamethrower == True and bing.lower() == "flamethrower":
                        print("You begin to use the flamethrower to burn down the door.")
                        print("As the fire burns, you realize it is starting to catch the walls on fire.")
                        print("You try to turn off the flamethrower but it continues to spit flames religiously.")
                        print("The ceiling saggs above you...")
                        print("'CRACK!'")
                        print("The ceiling splits open and the roof falls on top of you!")
                        print("A large wooden support beam smashes you in the head and knocks you out...")
                        print("As you come to however, you find yourself in your bed, safe and sound.")
                        done = True
                        break
                    elif bing.lower() == "flamethrower" and flamethrower == False:
                        print("You do not have a flamethrower smart guy.")
                    elif bing.lower() == "chainsaw" and chainsaw == True:
                        print("The chainsaw makes quick work of the door.")
                        print("When the door falls you throw the chainsaw away and sprint for the opening...")
                        print("As you reach the door however, your vision begins to swim...")
                        print("Right as you reach the door, you pass out.")
                        break
                    elif bing.lower() == "chainsaw" and chainsaw == False:
                        print("You do not have a chainsaw smart guy")
                    else:
                        print("You have nothing to use on the door and chose to continue on your path.")
                else:
                    print("You decide to avoid the door and continue seaching the house.")
            else:
                pass

        elif current_room == 8: #kitchen
            if bing.lower() == "investigate" or bing.lower() == "i":
                print("There is a large dark item on the kitchen table...")
                invest = input("Would you like to approach it? ")
                if invest.lower() == "yes" or invest.lower() == "y":
                    print("The item is a flamethrower!")
                    print("You add a flamethrower to your backpack.")
                    pack = [flamethrower]
                    backpack.append(pack)
                    flamethrower = True
                else:
                    print("You decide to avoid the dark object and continue on your investigations.")
            else:
                pass

        elif current_room == 9: #living room bathroom
            if bing.lower() == "investigate" or bing.lower() == "i":
                print("You start to feel a slight prickling sensation in the small of your back...")
                print("That prickling starts to feel warm as you touch it...")
                print("All of a sudden you smell it...")
                print("The smell of burning flesh.")
                print("You rip off your shirt as fast as you can, but your back is on fire.")
                print("You rush to the bathtub and cranck on the tap...")
                print("No water.")
                print("You rush to the sink")
                print("No water.")
                print("You scream in pain and hopelessness as you slowly are consumed by the flames and rendered into a steaming pile of ahses.")
                break
            else:
                pass

print("Thanks for playing!")