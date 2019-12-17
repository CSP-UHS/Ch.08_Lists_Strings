'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
# Murderer, Weapon, Place
room_list = []

room = ["You wake up in a strange place. Your only exit is locked. Find a way out and escape."
    , 1, None, None, None]
room_list.append(room)

room = ["You walk into the Ballroom, the walls are a bright gold. A grand piano sits on the left side of the room and a rose couch on the right.", None, 9, 0, 2]
room_list.append(room)

room = ["The Conservatory, its a quiet room. There are some plants and a small desk. You'll be suprised what you'll find if you look around. ", 3, None, 2, None]
room_list.append(room)

room = ["You are now in the Billard's room, nothing here but a pool table.", 4, None, 2, None]
room_list.append(room)

room = ["In the Library, a big table sits in the middle of the room. The walls are lined with books", 5, None, 4, None]
room_list.append(room)

room = ["The Study is peaceful, looking around you see a purple couch with a desk and a lamp. ", None, 6, 4, None]
room_list.append(room)

room = ["In the Hall is nothing but here but a small round table in the middle of the room. The walls are a bland cream, and floor is wooden. nothing here", None, 7, None, 5]   #
room_list.append(room)

room = ["You are now in the Lounge, Green couches line the room. The wall's are a bland color but the carpet is a bold blue", None, None, 8, 6]
room_list.append(room)

room = ["Walking into the Dining room, you see wood floors and a grand wooden table...but you smell something odd...wait is that blood?", 7, None, 9, None]
room_list.append(room)

room = ["You make it into the Kitchen, blood lines the floor, splattered in every place possible. You can barley see the light blue walls in all the red.\n"
        "A human torso sits in the middle of the room the organs spilling out of its chest cavity...the limbs have been all severed off, even the head."
        "Where is the rest of the body?", 8, None, None, 1]
room_list.append(room)
current_room = 0

inventory = []

key = 1 # in front room
head = 1 # in the ballroom
feet = 1 # Dining room
legs = 1 # HALL
arms = 1 # BILLARD ROOM
done = False

while done == False:
    print(room_list[current_room][0])
    print()
    if current_room == 2:   #Conservatory
        an = input("would you like to inspect the couch? Yes or No : ")
        if an.lower() == "yes" or an.lower() == "y":
            print("You walk over to the couch, and look around for any imperfections. You can find none, you almost walk away but then somthing catches your eye")
            print("scuff marks line the floor, You push the coach away from the wall, and see a secret entrance, where does it lead?\n")
            an = input("Would you like to go in the passage? Yes or No : ")
            if an.lower() == "yes" or an.lower() == "y":
                print("You open the secret entrance and jump in. There is nothing but darkness, you feel along the walls until you hit another door")
                current_room = 7
                print("Huh that's unusual, you end up in the Lounge.")
                print(room_list[current_room][0])
            else:
                print("sorry that's not an option")
        if an.lower() == "no" or an.lower() == "n":
            print("\nYou walk away from the coach, its not worth it. What was that old saying again.\n")
            print("O-h, curiosity killed the cat. Its best left untouched.")
        else:
            print("sorry that's not an option")
            ##########################################
    if current_room == 5:  # Study
        an = input("would you like to inspect the book shelves? Yes or No : ")
        if an.lower() == "yes" or an.lower() == "y":
            print("You touch each spine of the books and one falls out. You find a lever")
            print(" You pull it and a shelve slides out of the wall. A big wooden door, but where does it lead?")
            an = input("\nWould you like to go in the passage? Yes or No : ")
            if an.lower() == "yes" or an.lower() == "y":
                print("You walk until you feel another door")
                print("Huh that's unusual, you end up in the Kitchen.")
                current_room = 9
                print(room_list[current_room][0])
            else:
                print("sorry that's not an option")
        if an.lower() == "no" or an.lower() == "n":
            print("\nYou walk away from the door, its not worth it besides Curiosity killed the cat. Best left untouched.\n")
        else:
            print("sorry that's not an option")
            ##########################################
    if current_room == 7:  # Lounge
        an = input("would you like to inspect the couch? Yes or No : ")
        if an.lower() == "yes" or an.lower() == "y":
            print("You move the couch and find a secret entrance")
            print("There is a small wooden door, where does it lead?")
            an = input("\nWould you like to go in the passage? Yes or No : ")
            if an.lower() == "yes" or an.lower() == "y":
                print("You open the wooden door and walk until you find your way to the conservatory")
                current_room = 2
                print(room_list[current_room][0])
            else:
                print("sorry that's not an option")
        if an.lower() == "no" or an.lower() == "n":
            print("\nYou walk away from the trap. Its not worth it besides Curiosity killed the cat.\n")
        else:
            print("sorry that's not an option")
            ##########################################
    if current_room == 9:  # Conservatory
        an = input("would you like to inspect the pantry? Yes or No : ")
        if an.lower() == "yes" or an.lower() == "y":
            print("You open the pantry and it leads to a door")
            an = input("\nWould you like to go in the passage? Yes or No : ")
            if an.lower() == "yes" or an.lower() == "y":
                print("You open the wooden door and walk until you feel a smaller door")
                current_room = 5
                print("You open the door. Huh that's unusual, your in the Study.")
                print(room_list[current_room][0])
            else:
                print("sorry that's not an option")
        if an.lower() == "no" or an.lower() == "n":
            print("\nYou run away from the pantry, its not worth it. besides its covered in blood\n")
        else:
            print("sorry that's not an option")
            ##########################################
    if current_room == 1: ### FIND THE HEAD in BALLROOM
        an = input("What would you like to inspect? The piano or the coach: ")
        if an.lower() == "piano" or an.lower() == "p":
            print("you walk to the left side of the room, where the piano stands. There is nothing on the piano...")
            print("You lift up the lid of the piano and find a severed head. The dead eyes staring at you.")
            print("blood runs down its eyes, mouth and ears")
            an = input("Would you like to place the severed head in your inventory : ")
            if an.lower() == "yes" or an.lower() == "y":
                print("You place the head into your inventory")
                inventory.append("head")
            if an.lower() == "no" or an.lower() == "n":
                print("you slam the lid and leave the severed head in the piano")
            else:
                print("sorry that's not an option")
        if an.lower() == "coach" or an.lower() == "c":
            print("You walk up to the rose coach...everything seems in order")
        if an.lower() == "no" or an.lower() == "n":
            print("you don't inspect anything")
        else:
            print("sorry that's not an option")
            ##########################################
    if current_room == 3: ### ARMS in BILLARD ROOM
        an = input("Would you like to inspect the pool table? yes or no: ")
        if an.lower() == "yes" or an.lower() == "y":
            print("You look around the pool table, nothing seems out of the order until you hit a secret panel.")
            print("You reach under the table to feel something squishy. You look under the table and scream.")
            print("All you see are a pair of arms shoved into the panel")
            an = input("would you like to place the severed arms in your inventory?: ")
            if an.lower() == "yes" or an.lower() == "y":
                inventory.append("arms")
            if an.lower() == "no" or an.lower() == "n":
                print("you run away from the pool table")
            else:
                print("sorry that's not an option")
        if an.lower() == "no" or an.lower() == "n":
            print("You leave the pool table, best left untouched....")
        else:
            print("sorry that's not an option")
            ##########################################
    if current_room == 6: ### HALL find LEGS
        an = input("Would you like to inspect the room : ")
        if an.lower() == "yes" or an.lower() == "y":
            print("you walk around the room until you hear a squeaking noise from the floor boards you stand on")
            print("you knock on the wood and find its lose. You pry open the floor and find yourself staring at severed legs")
            an = input("Would you like to place the legs into your inventory: ")
            inventory.append("legs")
        if an.lower() == "no" or an.lower() == "n":
            print("You walk away and don't inspect the floor boards")
        else:
            print("sorry that's not an option")
            ##########################################
    if current_room == 8: ### Dining room find FEET
        an = input("would you like to inspect the dining room table? :")
        if an.lower() == "yes" or an.lower() == "y":
            print("You walk up to the table...you smell blood")
            print("You see two feet tied together by a red ribbon...who would do such a thing.")
            an = input("would you like to place the severed feet in your inventory? :")
            if an.lower() == "yes" or an.lower() == "y":
                inventory.append("feet")
                print("you have successfully put the feet in your inventory.")
            if an.lower() == "no" or an.lower() == "n":
                print("you run away from the table")
            else:
                print("sorry that's not an option")
        if an.lower() == "no" or an.lower() == "n":
            print("you run away from the table")
        else:
            print("sorry that's not an option")
            ##########################################
    direction = input("What direction would you like to go? N, E, S, W, open your inventory or quit: ")
    print()
    if direction.lower() == "inventory" or direction.lower() == "i":
        print(inventory)
    if direction.lower() == "north" or direction.lower() == "n":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You cant go that way")
        else:
            current_room = next_room
    elif direction.lower() == "east" or direction.lower() == "e":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You cant go that way")
        else:
            current_room = next_room
    elif direction.lower() == "south" or direction.lower() == "s":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You cant go that way")
        else:
            current_room = next_room
    elif direction.lower() == "west" or direction.lower() == "w":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You cant go that way")
        else:
            current_room = next_room
    if len(inventory) == 4:
        print("you hear a commotion in the house, all the light's flicker on and off.")
        print("A trail appears of blood leading to the kitchen")
        print("the dead body is now whole again. What does this mean")
        print()
        print("A secret passage has been opened somewhere in the house")
        inventory.remove("head")
        inventory.remove("feet")
        inventory.remove("legs")
        inventory.remove("arms")
        print("Find the passage")
    if current_room == 0:
        an = input("Would you like to take a look around? yes or no? :")
        if an.lower() == "yes" or an.lower() == "y":
            print("you find a golden key in the middle of the room")
            inventory+=key
    if len(inventory) == key and current_room == 4:
        an = input("Another door has appeared in the current room...do you want to look inside? yes or no: ")
        if an.lower() == "yes" or an.lower() == "y":
            print("you walk into the room there is nothing but a operating table and tools.")
            print("written in blood is You're next")
            print("the lights turn off and the exit slammed shut")
        if an.lower() == "no" or an.lower() == "n":
            print("You have made the wrong decision. Try again")
    if direction.lower() == "q":
        done = True

