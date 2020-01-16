'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game
'''

room_list = [] #Sets up empty room list to be added to later
room = ("You have entered the house. From here you must get to the bunker asap. The door-room has nothing in it.",1, None, None, None) #Doorway
room_list.append(room) #Adds the above room to list, used for every room
room = ("This living room has been long abandoned. The hallway to your left (west) looks promising.",None, 2, 0, 3) #Living Room
room_list.append(room)
room = ("The sunroom is filled with dirt.",5, None, None, 1) #Sunroom
room_list.append(room)
room = ("The twisted hallway leads to a heavy locked door that will require a key.",4, 1, None, None) #Hallway
room_list.append(room)
room = ("You unlock the door and keep moving forward. In keeping with most of the house, there is nothing of interest in this foyer.",6, None, 3, None) #Foyer
room_list.append(room)
room = ("This dark room has a skeleton in the corner, its mouth appears to be holding something, you examine it and find a key.",None, None, 2, None) #Darkroom
#Decided to automaticly give the player a key instead of forcing them to interact with a skelton because who wants to interact with a skeleton?
room_list.append(room)
room = ("Due to the horrible way I programmed this game, this text will never appear.",None, None, 4, None) #Bunker
room_list.append(room)

print("World War 3 has started and America is being attacked.") #Establishes a beleivable story to get the player emotionally invested
print("Your friend's house has a nuclear bunker and they are out of town so you decide to go there.")
print("Unluckily for you, their house is not very straightforward.")

current_room = 0 #Starting Location as doorway
next_room = 0 #sets up varibles for later
player_has_key = False
done = False
while not done: #Makes program run until stopped

    print()
    print(room_list[current_room][0]) #Tells player where thet curently are
    user_choice = input("Press N,E,S,W to move or Q to quit.") #Tells player how to interact with the game

    if user_choice.lower() == "north" or user_choice.lower() == "n": #allows the player to move north

       if current_room == 3 and player_has_key == False: #Super Janky way of checking if the player is in Room 3 with the key
        print("You do not have the key.")
        continue
       if current_room == 2: #Again really bad way to check if the player is in a certan room to give them a key, my really tired brain can't think of a better way lol
           player_has_key = True
       next_room = room_list[current_room][1]
       if current_room == 4: #checks if the player has won
            print("You have reached the bunker and are now safe!")
            print("Thanks for playing.")
            done = True

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

    elif user_choice.lower() == "quit" or user_choice.lower() == "q" or current_room == 6: #allows the player to quit
       print("Thanks for playing.")
       done = True

    else:
        print("Invalid input, try again.")