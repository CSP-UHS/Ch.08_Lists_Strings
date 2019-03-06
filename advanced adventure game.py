'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
print("You are aboard the Millennium Falcon and the galaxy is in great danger from The First Order.")
print("The galaxy needs Luke Skywalker to save everyone")
print("To find him you need to find the 2 fragments of a map")
player_input = input("Would you like instructions?\n\r")
if player_input.lower() == "yes":
    print("To play the game you need can enter phrases such as")
    print("North, East, South, West")
    print("Inventory, Grab, Give, Enter, Exit, and Help")

room_list = []
inventory = [None,None,None,None]
current_room = 0
done = False

def help():
    print()
    print("To play the game you need can enter phrases such as")
    print("North, East, South, West")
    print("Inventory, Grab, Give, Enter, Exit, and Help, for instructions")
    print()

room = ["You are orbiting a planet known as Naboo",None,1,2,None]    #These generate the map list
room_list.append(room)
room = ["You are orbiting Tatooine",None,None,6,0]
room_list.append(room)
room = ["You are near a big cluster of asteroids where Alderaan once was",0,6,3,None]
room_list.append(room)
room = ["You are orbiting a planet full of forests, Takodana",2,4,None,None]
room_list.append(room)
room = ["You are near Star-Killer base",6,None,5,3]
room_list.append(room)
room = ["You are near a fiery planet, Mustafar",4,None,None,None]
room_list.append(room)
room = ["You orbiting an icy planet, Hoth",1,None,4,None]
room_list.append(room)
while done == False:   #Loop for actual game
    print()
    print(room_list[current_room][0])
    player_input = input("What do you want to do?")
    if player_input.lower() == "n" or player_input.lower() == "north":
        next_room = room_list[current_room][1]
    elif player_input.lower() == "e" or player_input.lower() == "east":
        next_room = room_list[current_room][2]
    elif player_input.lower() == "s" or player_input.lower() == "south":
        next_room = room_list[current_room][3]
    elif player_input.lower() == "w" or player_input.lower() == "west":
        next_room = room_list[current_room][4]
    elif player_input.lower() == "q" or player_input.lower() == "quit":
        done = True
    elif player_input.lower() == "enter":
        if current_room == 0: #Commands for Naboo
            print("You fly down to a castle in Naboo and find a paper")
            if inventory[0] == "fragment" and inventory[1] == "fragment":
                inventory[0] = "map"
                inventory[1] = None
                print("The fragment have combined!")
            while True:
                player_input = input("What do you want to do?")

                if player_input.lower() == "grab":
                    print("You read the paper:")
                    print("It has been said that luke took several stops before disappearing")
                    print("He stopped at a cold area")
                    print("You can combine the pieces at naboo")
                    print("The note doesn't say anything more")
                    print("You set the paper down")
                elif player_input.lower() == "exit":
                    print("You fly out to orbit")
                    next_room = current_room
                    break
                elif player_input.lower() == "help":
                    print(help())
                elif player_input.lower() == "inventory":
                    for i in range(0,4):
                        print(inventory[i])
        elif current_room == 1: #Commands for Tatooine:
            print("You fly down to the oceans of sand")
            if not inventory[0] == "fragment" or not inventory[0] == "map":
                print("Someone comes up to you")
                print("They say they have a fragment to find Luke")
                print("But they want a lightsaber in return")
            while True:
                player_input = input("What do you want to do?")
                if player_input.lower() == "give":
                    print("Give what?")
                elif player_input.lower() == "give lightsaber":
                    if inventory[2] == "lightsaber":
                        print("They thank you")
                        print("You have received a fragment of the map!")
                        inventory[0] = "fragment"
                    else:
                        print("You don't have the lightsaber!")
                elif player_input.lower() == "exit":
                    print("You fly out to orbit")
                    next_room = current_room
                    break
                elif player_input.lower() == "help":
                    print(help())
                elif player_input.lower() == "inventory":
                    for i in range(0,4):
                        print(inventory[i])
        elif current_room == 2: #Commands for ALDERAAN
            print("You fly around clusters of asteroids")
            print("You look around an asteroid and something catches your eye")
            print("Gamers scattered everywhere...")
            while True:
                player_input = input("What do you want to do?")
                if player_input.lower() == "grab":
                    print("There is nothing to grab")
                elif player_input.lower() == "exit":
                    print("You fly out to orbit")
                    next_room = current_room
                    break
                elif player_input.lower() == "help":
                    print(help())
                elif player_input.lower() == "inventory":
                    for i in range(0,4):
                        print(inventory[i])
        elif current_room == 3: #COMMANDS FOR TAKODANA
            print("You fly down to a forest near a Cantina")
            print("You enter the Cantina and a really short angry lady comes up to you")
            print("She yells at you talking about the force")
            if not inventory[2] == "lightsaber":
                print("After a while of yelling she throws a lightsaber at your head")
                print("You black out")
                print("After a while you regain consciousness")
            inventory[2] = "lightsaber"
            while True:
                player_input = input("What do you want to do?")
                if player_input.lower() == "exit":
                    print("You fly out to orbit")
                    next_room = current_room
                    break
                elif player_input.lower() == "help":
                    print(help())
                elif player_input.lower() == "inventory":
                    for i in range(0,4):
                        print(inventory[i])
        elif current_room == 4: #COMMANDS FOR STAR-KILLER BASE
            if inventory[0] == "map":
                print("As you near the Star-Killer Base you hear a loud sound")
                print("You look around and notice the map is glowing")
                print("You look at the map and it becomes clear")
                print()
                player_input = input("Would you like to find luke?")
                if player_input.lower() == "yes":
                    print("You begin to start your hyper drive")
                    print("You zoom into hyper space")
                    print("As you exit hyperspace you see a Tropical Planet")
                    while True:
                        player_input = input("What do you want to do?")
                        if player_input.lower() == "exit":
                            print("You don't want to leave")
                        elif player_input.lower() == "help":
                            print(help())
                        elif player_input.lower() == "inventory":
                            for i in range(0, 3):
                                print(inventory[i])
                        elif player_input.lower() == "enter":
                            print("You fly towards this strange Tropical Planet")
                            print("Soon after you see a island with a mans silhouette")
                            print()
                            print("The End")
                            print()
                            quit()
                if player_input.lower() == "no":
                    print("You fly out to orbit")
                    continue
            else:
                print("You go near the Star-Killer Base")
                print("You don't feel the need to be here... yet")
                continue
        elif current_room == 5:
            print("You draw near this hot planet")
            print("You go to a energy facility")
            if not inventory[4] == "key":
                print("There you find a box with a key in it")
            while True:
                player_input = input("What do you want to do?")
                if player_input.lower() == "exit":
                    print("You fly out to orbit")
                    next_room = current_room
                    break
                elif player_input.lower() == "help":
                    print(help())
                elif player_input.lower() == "inventory":
                    for i in range(0,4):
                        print(inventory[i])
                elif player_input.lower() == "grab":
                    print("You grab the key")
                    inventory[4] = "key"
                elif player_input.lower() == "give":
                    print("Give what?")
                elif player_input.lower() == "give key":
                    print("You set down the key")
        elif current_room == 6:
            print("You fly down to a cold planet")
            print("You go to a cave")
            print("You find an old wampa arm")
            if not inventory[1] == "fragment":
                print("You find something buried in the dirt")
            while True:
                player_input = input("What do you want to do?")
                if player_input.lower() == "grab":
                    if not inventory[1] == "fragment":
                        print("You grab the thing buried in the sand")
                        print("You gained another piece to the map!")
                        inventory[1] = "fragment"
                    else:
                        print("There is nothing to grab")
                if player_input.lower() == "exit":
                    print("You fly out to orbit")
                    next_room = current_room
                    break
                elif player_input.lower() == "help":
                    print(help())
                elif player_input.lower() == "inventory":
                    for i in range(0,4):
                        print(inventory[i])
    elif player_input.lower() == "grab":
        print("There is nothing to grab")
        continue
    else:
        print()
        print("I can't apply this word")
        continue
    if next_room == None:
        print("You can't go that way!")
    else:
        current_room = next_room