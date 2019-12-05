'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
room_list = [] #empty ray of room list

room = ["Welcome to the front porch Detective, we need you to look at the body quickly! Go find the body", 2, None, None, None]   #THE COPY
room_list.append(room) #THE COPY

room = ["You are now in the South Hall", 5, 3, 0, 1]   #THE COPY
room_list.append(room) #THE COPY

room = ["You are now in the 2 Bedroom", 4, 2, None, None]   #THE COPY
room_list.append(room) #THE COPY

room = ["You are now in the South Hall", 5, 3, 0, 1]   #THE COPY
room_list.append(room) #THE COPY

room = ["You are now in the grand bedroom", None, 5, 1, None]   #Bed room 1
room_list.append(room) #THE COPY

room = ["You are now in the North Hall, it is elegent with red carpets lining the floor and frames of people on the walls", 7, 6, 2, 4]   #THE COPY
room_list.append(room) #THE COPY

room = ["You have walked into the kitchen to find blood splatter every where. The body lays on the floor face downwards a knife stuck in the cospes back", None, None, 3, 5]   #THE COPY
room_list.append(room) #THE COPY

room = ["You are now in the Dining room, but smell somthing odd...wait is that blood?", 6, None, None, 2]   #THE COPY
room_list.append(room) #THE COPY

current_room = 0

done = False

while False:
    print()
    room_list[current_room][0]
    print("Hello Detective! You have finally made it! I was worried you were lost, Please come and take a look at the body")
    direction =input("What direction would you like to go? N, E, S, W or Q for quit: ")
    if direction.lower() == "north" or direction.lower() == "n":
        next_room = room_list[current_room][1]

    elif direction.lower() == "east" or direction.lower() == "e":
        next_room = room_list[current_room][1]

    elif direction.lower() == "south" or direction.lower() == "s":
        next_room = room_list[current_room][1]

    elif direction.lower() == "west" or direction.lower() == "w":
        next_room = room_list[current_room][1]

    if next_room == None:
        print("You cant fo that way")
    else:
        current_room = next_room

    if direction.lower() == "q":
        done = True









