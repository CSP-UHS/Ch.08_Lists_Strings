'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
room_list = [] #empty ray of room list

room = ["Welcome to the front porch Detective. You have finally made it! We need you to look at the body quickly! Go find the body", 1, None, None, None]   #THE COPY
room_list.append(room) #THE COPY

room = ["You are now in the Ballroom", None, 9, 0, 2]   #THE COPY
room_list.append(room) #THE COPY

room = ["You are now in the Conservatory", 3, None, 2, None]   #THE COPY
room_list.append(room) #THE COPY

room = ["You are now in the Billard room", 4, None, 2, None]   #THE COPY
room_list.append(room) #THE COPY

room = ["You are now in the Library", 5, None, 4, None]   #THE COPY
room_list.append(room) #THE COPY

room = ["You are now in the Study", None, 6, 4, None]   #Bed room 1
room_list.append(room) #THE COPY

room = ["You are now in the Hall", None, 7, None, 5]   #Bed room 1
room_list.append(room) #THE COPY

room = ["You are now in the Lounge", None, None, 8, 6]   #THE COPY
room_list.append(room) #THE COPY

room = ["You are now in the Dining room, but smell somthing odd...wait is that blood?", 7, None, 9, None]   #THE COPY
room_list.append(room) #THE COPY

room = ["You have walked in the Kitchen", 8, None, None, 1]   #THE COPY
room_list.append(room) #THE COPY

current_room = 0

done = False

while done == False:
    print(room_list[current_room][0])
    print()
    direction =input("What direction would you like to go? N, E, S, W or Q for quit: ")
    if direction.lower() == "north" or direction.lower() == "n":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You cant fo that way")
        else:
            current_room = next_room
    elif direction.lower() == "east" or direction.lower() == "e":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You cant fo that way")
        else:
            current_room = next_room
    elif direction.lower() == "south" or direction.lower() == "s":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You cant fo that way")
        else:
            current_room = next_room
    elif direction.lower() == "west" or direction.lower() == "w":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You cant fo that way")
        else:
            current_room = next_room
    if direction.lower() == "q":
        done = True









