'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
#NORTH EAST SOUTH WEST
room_list=[]
#Create rooms and add to room list
room=["You are on the front porch.",2,None,None,None]
room_list.append(room)
room=["You are in Bedroom 2.",4,2,None,None]
room_list.append(room)
room=["You are in the South Hall.",5,3,0,1]
room_list.append(room)
room=["You are in the Dining Room.",6,None,None,2]
room_list.append(room)
room=["You are in Bedroom 1.",None,5,1,None]
room_list.append(room)
room=["You are in the North Hall",7,6,2,4]
room_list.append(room)
room=["You are in the Kitchen.",None,None,3,5]
room_list.append(room)
room=["You are on the Balcony.",None,None,5,None]
room_list.append(room)

current_room = 0

#directions

done = False
while not done:
    print()
    print(room_list[current_room][0])
    direction = input("Where do you want to go? N,E,W,S directions or Q to quit: ")

    #NORTH
    if direction.lower()=="n" or direction.lower()== "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print()
            print("You can't go that way!")
        else:
            current_room = next_room
    #EAST
    elif direction.lower()=="e" or direction.lower()== "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print()
            print("You can't go that way!")
        else:
            current_room = next_room

    #SOUTH
    elif direction.lower()=="s" or direction.lower()== "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print()
            print("You can't go that way!")
        else:
            current_room = next_room
    #WEST
    elif direction.lower()=="w" or direction.lower()== "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print()
            print("You can't go that way!")
        else:
            current_room = next_room

    #QUIT
    elif direction.lower() == "q" or direction.lower() == "quit":
        done=True

    #STUPID
    else:
        print("Not sure you understand what you are doing")

print("Thanks for playing!")