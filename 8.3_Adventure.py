'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game
'''

room_list = [] #Sets up empty room list to be added to later
room = ("You are in the house's only entrance, but now you must try to escape!",1, None, None, None) #Doorway
room_list.append(room) #Adds the above room to list, used for every room
room = ("The living room has been long abandoned.",None, 2, 0, 3) #Living Room
room_list.append(room)
room = ("The sunroom is filled with dirt.",5, None, None, 1) #Sunroom
room_list.append(room)
room = ("The twisted hallway leads to a heavy door.",4, 1, None, None) #Hallway
room_list.append(room)
room = ("From the Foyer you can see the bunker north of you",6, None, 3, None) #Foyer
room_list.append(room)
room = ("This dark room has a skeleton in the corner.",None, None, 2, None) #Darkroom
room_list.append(room)
room = ("Congratulations, you reached the bunker and are now safe!",None, None, 4, None) #Bunker
room_list.append(room)

current_room = 0 #Starting Location as doorway
next_room = 0 #sets up varible for later
done = False
while not done: #Makes program run until stopped

    print()
    print(room_list[current_room][0]) #Tells player where thet curently are
    user_choice = input("Press N,E,S,W to move or Q to quit.") #Tells player how ot interact with the game

    if user_choice.lower() == "north" or user_choice.lower() == "n": #allows the player to move north
       next_room = room_list[current_room][1]
       if next_room == None:
           print("There is no room in that direction, try a different way.")
       else: current_room = next_room

    elif user_choice.lower() == "east" or user_choice.lower() == "e": #allows the player to move east
       next_room = room_list[current_room][2]
       if next_room == None:
           print("There is no room in that direction, try a different way.")
       else: current_room = next_room

    elif user_choice.lower() == "south" or user_choice.lower() == "s": #allows the player to move south
       next_room = room_list[current_room][3]
       if next_room == None:
           print("There is no room in that direction, try a different way.")
       else: current_room = next_room

    elif user_choice.lower() == "west" or user_choice.lower() == "w": #allows the player to move west
       next_room = room_list[current_room][4]
       if next_room == None:
           print("There is no room in that direction, try a different way.")
       else: current_room = next_room

    elif user_choice.lower() == "quit" or user_choice.lower() == "q": #allows the player to move quit
       print("Thanks for playing.")
       done = True

    else:
        print("Invalid input, try again.")