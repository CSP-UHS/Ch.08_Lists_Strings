'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
room_list = []
# Create Rooms and add to room list
room = ["You are on the front porch.", 2, None, None, None]
room_list.append(room)
room = ["You are in Bedroom 2", 4, 2, None, None]
room_list.append(room)
room = ["You are in the South Hall", 5, 3, 0, 1]
room_list.append(room)
room = ["You are in the Dining Room", 6, None, None, 2]
room_list.append(room)

current_room = 0
done = False
while not done:
    print()
    print(room_list[current_room][0])
    bing = input("Type N, E, W, S, direction or Q to quit\n")

    # NORTH
    if bing.lower() == "n" or bing.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You cannot go that way")
        else:
            current_room = next_room
    # EAST
    if bing.lower() == "e" or bing.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You cannot go that way")
        else:
            current_room = next_room
    # SOUTH
    if bing.lower() == "s" or bing.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You cannot go that way")
        else:
            current_room = next_room
    # WEST
    if bing.lower() == "w" or bing.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You cannot go that way")
        else:
            current_room = next_room
    #QUIT
    elif bing.lower() == "q" or bing.lower() == "quit":
        done = True
    #STUPID
    # else:
    #     print("You are stupid!!!!!!!!1 You don't understand what you are doing!!!!")

print("Thanks for playing!")
