'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''

room_list = []
#create rooms and add to room list
room = ["You are in the master bedroom.", ]#North #East #South #West
room_list.append(room)

room = ["You are in the closet.", ]
room_list.append(room)

room = ["You are in the master bathroom", ]
room_list.append(room)

room = ["You are in the kitchen hallway", ]
room_list.append(room)

room = ["You are in the livingroom hallway", ]
room_list.append(room)

room = ["You are in the ", ]
room_list.append(room)

room = ["You are in the ", ]
room_list.append(room)


current_room = 0
done = False
while not done:
    print()
    print(room_list[current_room][0])
    bing = input("")

    #North
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

    #South
    elif bing.upper() == "S" or bing.upper() == "SOUTH":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way!")
        else:
            current_room = next_room

    #West
    elif bing.upper() == "W" or bing.upper() == "WEST":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way!")
        else:
            current_room = next_room
    #QUIT
    elif bing.lower() == "q" or bing.lower() == "quit":
        done = True

    #STUPID
    else:
        print("Not sure you understand the game pal.")

print("Thanks for playing!")