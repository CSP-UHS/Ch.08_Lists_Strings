'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
room_list = []

room = ["\nWelcome to the front porch Detective. You have finally made it! We need you to look at the body quickly! Go find the corpse.", 1, None, None, None]
room_list.append(room)

room = ["You walk into the Ballroom, the walls are a bright gold. A grand piano sits on the left side of the room and a rose couch on the right.", None, 9, 0, 2]
room_list.append(room)

room = ["You are now in the Conservatory, its a quiet room. There are some plants and a small desk. You'll be suprised what you'll find if you look around. ", 3, None, 2, None]
room_list.append(room)

room = ["You are now in the Billard's room, nothing here but a pool table.", 4, None, 2, None]
room_list.append(room)

room = ["In the Library, a big table sits in the middle of the room. The walls are lined with books", 5, None, 4, None]
room_list.append(room)

room = ["The Study is peaceful, looking around you see a purple couch with a desk and a lamp. ", None, 6, 4, None]
room_list.append(room)

room = ["You are now in the Hall, nothing here but a small round table in the middle of the room. The wall are a bland cream, and floor is wooden. nothing here", None, 7, None, 5]   #
room_list.append(room)

room = ["You are now in the Lounge, Green couches line the room. The wall's are a bland color but the carpet is a bold blue", None, None, 8, 6]
room_list.append(room)

room = ["Walking into the Dining room, you see wood floors and a grand wooden table...but you smell something odd...wait is that blood?", 7, None, 9, None]
room_list.append(room)

room = ["You make it into the Kitchen, blood lines the floor, splattered in every place possible. You can barley see the light blue walls in all the red.\n"
        "But what happened to the body....", 8, None, None, 1]
room_list.append(room)

current_room = 0
done = False
inventory = []

while done == False:
    print(room_list[current_room][0])
    print()
    if current_room == 2:   #Conservatory
        an = input("would you like to inspect the couch? Yes or No : ")
        if an.lower == "yes" or an.lower == "y":
            print("You walk over to the couch, you look around for any imperfections. You can find none, you almost walk away but then somthing catches your eye")
            print("there are scuff marks on the floor, you push the coach away from the wall, and see a secret entrance, where does it lead?")
            print()
            an = input("Would you like to go in the passage? Yes or No : ")
            if an.lower == "yes" or an.lower == "y":
                print("You open the wooden door and jump through. its nothing but darkness inside, you feel against the walls until you hit another door")
                current_room = 7
                print(current_room)
                print("You open the door. Huh that's unusual, you end up in the Lounge.")
        if an.lower == "no" or an.lower == "n":
            print("you walk away from the coach, its not worth it. What was that old saying again, O-h, curiosity killed the cat. Its best left untouched.")
    direction =input("What direction would you like to go? N, E, S, W or Q for quit: ")
    print()
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
    if direction.lower() == "q":
        done = True









