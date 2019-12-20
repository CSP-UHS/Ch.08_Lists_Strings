'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''

current_room = 0
room_list = []
inventory = []
done = False

##  Rooms + Appending to room_list
room = ["You are in the foyer.", 4, 2, None, 1]  #Foyer
room_list.append(room)
room = ["Welcome to the guest bedroom.", 3, 0, None, None]  #Guest Bedroom
room_list.append(room)
room = ["Welcome to the kitchen.", 5, None, None, 0]  #Kitchen
room_list.append(room)
room = ["Welcome to the bathroom.", 6, 4, 1, None]  #Bathroom
room_list.append(room)
room = ["Welcome to the living room.", 7, 5, 0, 3]  #Living Room
room_list.append(room)
room = ["Welcome to the dining room.", 8, None, 2, 4]  #Dinig Room
room_list.append(room)
room = ["Welcome to the master bedroom.", None, 7, 3, None]  #Master Bedroom
room_list.append(room)
room = ["Welcome to the hallway.", None, 8, 4, 6]  #Hallway
room_list.append(room)
room = ["Welcome to the library.", None, None, 5, 7] #Library
room_list.append(room)
##  End of appending to room_list


player_name = input("What is your name? >   ") #player name
print(player_name.center(40), "\n")

while not done:
    print()
    print(room_list[current_room][0])
    print("Which direction would you like to go", player_name, "?")
    direction = input("\n N for north \n E for east \n S for south \n W for west \n Q to quit \n  ")


    if direction.lower() == 'n' or direction.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way.")
        else:
             current_room = next_room

    elif direction.lower() == "east" or direction.lower() == "e":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way")
        else:
             current_room = next_room

    elif direction.lower() == "south" or direction.lower() == "s":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room

    elif direction.lower() == "west" or direction.lower() == "w":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room

    elif direction.lower() == "q":
        print("Thanks for playing!")
        done = True

    else:
        print()
        print("Invalid choice. Please try again.")
        print()
        continue

##      Investigate in foyer
    if current_room == 0:
        search = input("Would you like to search the room?")
        if search.lower() == "yes" or search.lower() == "y":
            print("There is a painting on the wall of a man and woman, and there is a mat in front of the front door")
            while not done:
                 invest = input("Would you like to check under the mat or behind the painting? Type 'none' if you do not want to do investigate.")
                 if invest.lower == "mat":
                   print("There is a letter under the mat that reads:")



