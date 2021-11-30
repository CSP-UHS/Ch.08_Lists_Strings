'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''



room_list = []
# Create rooms and add to list

room = ["You are on the front porch,",2,None, None, None]
room_list.append(room)
room = ["two,",4,2, None, None]
room_list.append(room)
room = ["North,",5,3,0,1,]
room_list.append(room)
room = ["East,",6, None, None , 2]
room_list.append(room)

current_room = 0

done = False
while not done:
    print()
    print(room_list[current_room][0])
    bing = input("Type N, E, W, S directions or Q to quit")

    #NORTH
    if bing.lower()=="n" or bing.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go there dummy")
        else:
            current_room = next_room
    #EAST
    elif bing.lower() == "e" or bing.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go there dummy")
        else:
            current_room = next_room
    #SOUTH
    elif bing.lower() == "s" or bing.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go there dummy")
        else:
            current_room = next_room
    #WEST
    elif bing.lower() == "w" or bing.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go there dummy")
        else:
            current_room = next_room
    #QUIT
    elif bing.lower() == "Q" or bing.lower() == "quit":
        done = True
    #STUID
    else:
        print("That didn't make any sense, can you actually read please? Or let me know that there is something wrong with my code")
