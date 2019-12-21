'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
# Murderer, Weapon, Place
room_list = []

room = ["\nYou wake up in a strange place. Your only exit is locked. You need to find a way out and escape. You realize that you're in the Front room.\n"
        "There is a note on the door 'Find all the body parts to complete my masterpiece'.", 1, None, None, None]
room_list.append(room)

room = ["You walk into the Ballroom, the walls are bright gold. A grand piano sits on the left side of the room and a rose couch on the right.", None, 9, 0, 2]
room_list.append(room)

room = ["The Conservatory is a quiet room, with plants and a small desk. You'll be surprised what you'll find if you look around. ", 3, 1, None, None]
room_list.append(room)

room = ["You are now in the Billard's room. A pool table stands in the room.", 4, None, 2, None]
room_list.append(room)

room = ["In the Library, a table sits in the middle of the room. The walls are lined with books", 5, None, 4, None]
room_list.append(room)

room = ["The Study is peaceful, looking around you see a purple couch with a desk and a lamp. ", None, 6, 4, None]
room_list.append(room)

room = ["You are now in the Hall, there is nothing but a small round table. The walls are a cream, the floor wooden.", None, 7, None, 5]   #
room_list.append(room)

room = ["You are now in the Lounge, green couches line the room. The walls are a bland color but the carpet is a bold blue", None, None, 8, 6]
room_list.append(room)

room = ["Walking into the Dining room, you see table fit for ten people...but you smell something odd...wait is that blood?", 7, None, 9, None]
room_list.append(room)

room = ["You make it into the Kitchen, blood lines the floor, splattered in every place possible. You can barely see the light blue walls in all the red.\n"
        "A human torso sits in the middle of the room the organs spilling out of its chest cavity...the limbs have been all cut off, even the head."
        "Where is the rest of the body?", 8, None, None, 1]
room_list.append(room)
current_room = 0

inventory = []
turn = 0
key = 1 # in front room
key = False
head = 1 # in the ballroom
head = False
feet = 1 # Dining room
feet = False
legs = 1 # HALL
legs = False
arms = 1 # BILLARD ROOM
arms = False
done = False
fullbody = False

while done == False:
    print(room_list[current_room][0])
    print()
    if current_room == 2:   #Conservatory
        an = input("would you like to inspect the couch? Yes or No : ")
        if an.lower() == "yes" or an.lower() == "y":
            print("You walk over to the couch, and look around for any imperfections. You can find none, you almost walk away but somthing catches your eye.")
            print("Scuff marks line the floor. You push the couch away from the wall and see a secret entrance.\n")
            an = input("Would you like to go in the passage? Yes or No : ")
            if an.lower() == "yes" or an.lower() == "y":
                print("You open the secret entrance and walk in. no light reaches the tunnel, you feel along the wall until you hit another door")
                current_room = 7
                print("Huh that's unusual, you are in the Lounge.")
                print(room_list[current_room][0])
            elif an.lower() == "no" or an.lower() == "n":
                print("You walk away from the secret passage and put the couch back")
            else:
                print("sorry that's not an option")
        elif an.lower() == "no" or an.lower() == "n":
            print("\nYou walk away from the couch, and push it back into its original place.")
            print("Its not worth it. What was that old saying again.\n")
            print("O-h, curiosity killed the cat.")
        else:
            print("sorry that is not an option")
            ##########################################
    if current_room == 5:  # Study
        an = input("would you like to inspect the bookshelves ? Yes or No : ")
        if an.lower() == "yes" or an.lower() == "y":
            print("You touch every spine but one stands out. You pull on it and a shelf slides out of the wall")
            print("A wooden door appears, but where does it lead?")
            an = input("\nWould you like to go in the passage? Yes or No : ")
            if an.lower() == "yes" or an.lower() == "y":
                print("You walk in the tunnel until you find another door")
                print("Huh that's unusual, you're in the Kitchen.")
                current_room = 9
                print(room_list[current_room][0])
            elif an.lower() == "no" or an.lower() == "n":
                print("You walk away and the shelf slides back into the wall. Its best left untouched")
            else:
                print("sorry that's not an option")
        elif an.lower() == "no" or an.lower() == "n":
            print("\nYou walk away from the door, its not worth it.\n")
        else:
            print("sorry that is not an option")
            ##########################################
    if current_room == 7:  # Lounge
        an = input("would you like to inspect the couch, Yes or No : ")
        if an.lower() == "yes" or an.lower() == "y":
            print("You move the couch and find a secret entrance")
            print("There is a small wooden door, where does it lead?")
            an = input("\nWould you like to go in the passage? Yes or No : ")
            if an.lower() == "yes" or an.lower() == "y":
                print("You open the passage and walk until you find your way to the conservatory")
                current_room = 2
                print(room_list[current_room][0])
            elif an.lower() == "no" or an.lower() == "n":
                print("You walk away, and put the couch back")
            else:
                print("sorry that's not an option")
        elif an.lower() == "no" or an.lower() == "n":
            print("\nYou walk away from the trap, and put the couch back into its original place.\n")
        else:
            print("sorry that is not an option")
            ##########################################
    if current_room == 9:  # Conservatory
        an = input("would you like to inspect the pantry? Yes or No : ")
        if an.lower() == "yes" or an.lower() == "y":
            print("You open the pantry and see a door")
            an = input("\nWould you like to go in the passage? Yes or No : ")
            if an.lower() == "yes" or an.lower() == "y":
                print("You open the wooden door and walk until you feel a smaller door")
                current_room = 5
                print(" Huh that's unusual, you find yourself in the Study.")
                print(room_list[current_room][0])
            if an.lower() == "no" or an.lower() == "n":
                print("\nYou run away from the pantry, and close the doors. Besides its covered in blood\n")
        elif an.lower() == "no" or an.lower() == "n":
            print("You walk away and shut the door")
        else:
            print("sorry that is not an option")
            ##########################################
    if current_room == 1: ### FIND THE HEAD in BALLROOM
        an = input("What would you like to inspect, the piano, the couch or No?: ")
        if an.lower() == "piano" or an.lower() == "p":
            if head == False:
                print("you walk to the left side of the room, where the piano stands. There is nothing on the piano...")
                print("You lift up the lid and find a severed head. The dead eyes stare at you, while blood runs down it's orifices.")
                an = input("Would you like to place the severed head in your inventory : ")
                if an.lower() == "yes" or an.lower() == "y":
                    print("You place the head into your inventory")
                    inventory.append("head")
                    head = True
                elif an.lower() == "no" or an.lower() == "n":
                    print("You slam the lid and leave the severed head in the piano")
            else:
                print("You have already found the head")
        elif an.lower() == "couch" or an.lower() == "c":
            print("You walk up to the rose couch...everything seems in order")
        elif an.lower() == "no" or an.lower() == "n":
            print("you don't inspect anything")
        else:
            print("sorry that is not an option")
            ##########################################
    if current_room == 3: ### ARMS in BILLARD ROOM
        an = input("Would you like to inspect the pool table? yes or no: ")
        if an.lower() == "yes" or an.lower() == "y":
            if arms == False:
                print("You look at the pool table, nothing seems out of the order until you hit a secret panel lose.")
                print("You reach under the table and feel something squishy. You look under and scream.")
                print("All you can see are a pair of severed arms shoved into the small panel")
                an = input("would you like to place the arms in your inventory?: ")
                if an.lower() == "yes" or an.lower() == "y":
                    inventory.append("arms")
                    arms = True
                elif an.lower() == "no" or an.lower() == "n":
                    print("You slam the panel shut and run away")
            else:
                print("Nothing is here")
        elif an.lower() == "no" or an.lower() == "n":
            print("You leave the table alone...best left untouched....")
        else:
            print("sorry that is not an option")
            ##########################################
    if current_room == 6: ### HALL find LEGS
        an = input("Would you like to inspect the room, yes or no? : ")
        if an.lower() == "yes" or an.lower() == "y":
            if legs == False:
                print("you walk around the room until you hear a squeaking noise from the floor boards below you")
                print("you knock on the wood and pry open the floor finding yourself staring at two bloody legs")
                an = input("Would you like to place the legs into your inventory: ")
                if an.lower() == "yes" or an.lower() == "y":
                    print("You place both legs into your inventory")
                    inventory.append("legs")
                    legs = True
                if an.lower() == "no" or an.lower() == "n":
                    print("You place the boards back into place and slowly walk away")
            else:
                print("Nothing seems out of place")
        elif an.lower() == "no" or an.lower() == "n":
            print("You walk away and do not inspect the room")
        else:
            print("sorry that is not an option")
            ##########################################
    if current_room == 8: ### Dining room find FEET
        an = input("would you like to inspect the dining room table, yes or no? :")
        if an.lower() == "yes" or an.lower() == "y":
            if feet == False:
                print("You walk up to the table...you smell blood")
                print("You see two feet tied together by a red ribbon...who would do such a thing.")
                an = input("would you like to place the severed feet in your inventory? :")
                if an.lower() == "yes" or an.lower() == "y":
                    inventory.append("feet")
                    print("you have successfully put the feet in your inventory.")
                elif an.lower() == "no" or an.lower() == "n":
                    print("you run away from the table")
                else:
                    print("sorry that's not an option")
            else:
                print("nothing seems out of place")
        elif an.lower() == "no" or an.lower() == "n":
            print("you run away from the table")
        else:
            print("sorry that's not an option")
            ##########################################
    direction = input("\nWhat direction would you like to go? N, E, S, W, i for inventory or q for quit: ")
    print()
    if direction.lower() == "inventory" or direction.lower() == "i":
        print(inventory)
    if direction.lower() == "north" or direction.lower() == "n":
        next_room = room_list[current_room][1]
        turn+=1
        if next_room == None:
            print("You cant go that way")
        else:
            current_room = next_room
    elif direction.lower() == "east" or direction.lower() == "e":
        next_room = room_list[current_room][2]
        turn += 1
        if next_room == None:
            print("You cant go that way")
        else:
            current_room = next_room
    elif direction.lower() == "south" or direction.lower() == "s":
        next_room = room_list[current_room][3]
        turn += 1
        if next_room == None:
            print("You cant go that way")
        else:
            current_room = next_room
    elif direction.lower() == "west" or direction.lower() == "w":
        next_room = room_list[current_room][4]
        turn += 1
        if next_room == None:
            print("You cant go that way")
        else:
            current_room = next_room
    if len(inventory) == 4:
        print("You hear a commotion in the house, all the light's flicker on and off.")
        print("A trail of blood appears leading to the kitchen")
        print("the dead body is now complete. What does this mean")
        print()
        print("A secret passage has been opened somewhere in the house")
        print("Find the key to open the door")
        inventory.remove("head")
        inventory.remove("feet")
        inventory.remove("legs")
        inventory.remove("arms")
        fullbody = True
        print("Find the passage")
    if current_room == 0 and fullbody == True:
        an = input("Would you like to take a look around? yes or no? :")
        if an.lower() == "yes" or an.lower() == "y":
            print("you find a golden key in the middle of the room\n")
            inventory.append("Key")
            key = True
    if key == True and current_room == 4:
        an = input("Another door has appeared in your current room...do you want to look inside? yes or no: ")
        if an.lower() == "yes" or an.lower() == "y":
            print("you walk into the room, there is nothing but a operating table and surgical tools.")
            print("written in blood on the wall is You're next")
            print("the lights turn off and the exit is slammed shut")
            done = True
        if an.lower() == "no" or an.lower() == "n":
            print("You have made the Wrong decision. Try again")
    if direction.lower() == "q":
        done = True