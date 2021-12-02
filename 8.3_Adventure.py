'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
room_list=[]
room=["This is your starting room", 1, 2, 3, 4]
room_list.append(room)
room=["This is the dining hall", None, None, 0, 6]
room_list.append(room)
room=["This is the basement", None, None, None, 0]
room_list.append(room)
room=["This is the west hallway", 0, None, None, 9]
room_list.append(room)
room=["This is your bedroom", 6, 0, 9, None]
room_list.append(room)
room=["This is the porch", 10, None, None, None]
room_list.append(room)
room=["This is the east hallway", 7, 1, 4, 10]
room_list.append(room)
room=["This is the kitchen", None, 8, 6, None]
room_list.append(room)
room=["This is the kitchen freezer", None, None, None, 7]
room_list.append(room)
room=["This is your bathroom", 4, 3, None, None]
room_list.append(room)
room=["This is the living room", None, 6, 5, None]
room_list.append(room)



current_room=0
done=False
while done != True:
    print(" ")
    print(room_list[current_room][0])
    pIn = str(input("Do you wish to go North, South, West, East, or quit?"))
    if pIn.upper() == "N" or pIn.upper() == "North":
        next_room = room_list[current_room][4]
    elif pIn.upper() == "S" or pIn.upper() == "South":
        next_room = room_list[current_room][2]
    elif pIn.upper() == "E" or pIn.upper() == "East":
        next_room = room_list[current_room][1]
    elif pIn.upper() == "W" or pIn.upper() == "West":
        next_room = room_list[current_room][3]
    if next_room == None:
        print("You can't go that way")
    else:
        current_room = next_room