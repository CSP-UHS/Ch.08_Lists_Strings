'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
room_list=[]
#create rooms and add to rrom list
room = ["You are on the front porch.",2,None,None,None]
room_list.append(room)
room = ["You are in bedroom 2.",4,2,None,None]
room_list.append(room)
room = ["You are in the south hall.",5,3,0,1]
room_list.append(room)
room = ["You are in the dining room.",6,None,None,2]
room_list.append(room)
room = ["You are in the bedroom 1.",None,5,1,None]
room_list.append(room)
room = ["You are in the North hall.",7,6,2,4]
room_list.append(room)
room = ["You are in the kitchen.",None,None,3,5]
room_list.append(room)
room = ["You are in the dining room.",None,None,5,None]
room_list.append(room)


current_room = 0
done = False
while not done:
    print()
    print(room_list[current_room][0])
    bing = input("Type N, E, W, S, D for directions, or Q to quit")

    #north
    if bing.lower=="n" or bing.lower=="north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("Your can't go that waya")
        else:
            current_room = next_room

    # east
    if bing.lower == "e" or bing.lower == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("Your can't go that waya")
        else:
            current_room = next_room

#south
    if bing.lower=="s" or bing.lower=="south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("Your can't go that waya")
        else:
            current_room = next_room

#west
    if bing.lower=="w" or bing.lower=="west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("Your can't go that waya")
        else:
            current_room = next_room

#quit
    elif bing.lower()=="q" or bing.lower()=="quit":
        done = True

#stupid
    else:
        print("You cannot do that")