'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
print("This is a text-based adventure game")
room_list = []
current_room = 0
done = False
room = ["You are standing in the middle of a forest",None,2,3,None]    #These generate the map list
room_list.append(room)
room = ["You stand in a stream",None,None,None,1]
room_list.append(room)
room = ["You find yourself in a open area of the forest",1,None,4]
room_list.append(room)
room = ["You find youself in a single room log cabin",3,5,None,None]
room_list.append(room)
room = ["You at the outskirts of the forest at a road",None,None,None,4]
room_list.append(room)
while done == False:   #Loop for actual game
    print()
    print(room_list[current_room][0])
    player_input = input("Which direction would you like to go?\n\rN: North\n\rE: East\n\rS: South\n\rW: West\n\rQ: Quit\n\r")
    if player_input.lower() == "n" or player_input.lower() == "north":                                                                                         #If player goes NORTH
        next_room = room_list[current_room][1]  #Sets next room to direction north of current room
    elif player_input.lower() == "e" or player_input.lower() == "east":                                                                                       #If player goes EAST
        next_room = room_list[current_room][2]
    elif player_input.lower() == "s" or player_input.lower() == "south":                                                                                       #If player goes SOUTH
        next_room = room_list[current_room][3]
    elif player_input.lower() == "w" or player_input.lower() == "west":                                                                                       #If player goes WEST
        next_room = room_list[current_room][4]
    elif player_input.lower() == "q" or player_input.lower() == "quit":
        done = True
    if next_room == None:  #Thinks everytime if the player can move in the direction chosen
        print("You can't go that way!")
    else:
        current_room = next_room #Sets current room to next room