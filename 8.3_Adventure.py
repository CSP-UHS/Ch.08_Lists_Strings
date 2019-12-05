'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
room_list = []

room = ["Welcome to the front porch Detective. You have finally made it! We need you to look at the body quickly! Go find the body", 1, None, None, None]
room_list.append(room)

room = ["You walk into Ballroom, the walls are a bright gold, with a grand piano, and a rose couch", None, 9, 0, 2]
room_list.append(room)

room = ["You are now in the Conservatory, its a quit room. There are some plants and a small desk. You'll be suprised what you find ", 3, None, 2, None]
room_list.append(room)

room = ["You are now in the Billard room, nothing here but a pool table", 4, None, 2, None]
room_list.append(room)

room = ["You are now in the Library, a big table sits in the middle of the room. The walls are lined with books", 5, None, 4, None]
room_list.append(room)

room = ["The Study is peacefull, there is a purple couch and a desk with a lamp. ", None, 6, 4, None]
room_list.append(room)

room = ["You are now in the Hall, nothing here but a small round table in the middle of the room.", None, 7, None, 5]   #
room_list.append(room)

room = ["You are now in the Lounge, green couches line the room, the wall is a bland color but the carpet is a bold blue", None, None, 8, 6]
room_list.append(room)

room = ["You are now in the Dining room, wood floors and bland walls...but you smell something odd...wait is that blood?", 7, None, 9, None]
room_list.append(room)

room = ["You have walked in the Kitchen, blood lines the floor. Splattered in every place possible, you can barley see the light blue walls in all the red.\n"
        "But what happed to the body....", 8, None, None, 1]
room_list.append(room)

current_room = 0
done = False

while done == False:
    print(room_list[current_room][0])
    print()
    direction =input("What direction would you like to go? N, E, S, W or Q for quit: ")
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









