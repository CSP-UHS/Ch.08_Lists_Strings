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
room = ["You are in the grocery store parking lot, it is fairly empty and you can see the sun setting "
        "over the building.",1,None,None,None]
room_list.append(room)
room=["You walk into the entrance, for some reason the sliding doors are broken,"
      "so you take the manual doors.",3,None,None,None]
room_list.append(room)
room=["You go over to the cash registers, there is no one there to serve you.",6,2,1,4]
room_list.append(room)
room=["You go over to the deli, you smell the fresh food ready to be eaten.",None,None,3,5]
room_list.append(room)
room=["You walk to the employee breakroom, the door appears to be shut.",None,None,None,3]
room_list.append(room)
room=["You walk into the frozen food aisle, it is very cold here.",None,6,2,None]
room_list.append(room)
room=["You go to the regular food aisle, the shelves appear to be empty except one lonely "
      "box of cereal.",5,3,None,None]
room_list.append(room)

current_room = 0
backpack = []








done=False
while not done:

    print()
    print(room_list[current_room][0])
    direction = input("What do you want to do? N,E,W,S, interact, backpack, or Q to quit: ")

    #North
    if direction.lower() == "n" or direction.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print()
            print("You can't go that way!")
        else:
            current_room = next_room
        # EAST
    elif direction.lower() == "e" or direction.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print()
            print("You can't go that way!")
        else:
            current_room = next_room

    # SOUTH
    elif direction.lower() == "s" or direction.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print()
            print("You can't go that way!")
        else:
            current_room = next_room
    # WEST
    elif direction.lower() == "w" or direction.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print()
            print("You can't go that way!")
        else:
            current_room = next_room


    #Interact
    elif direction.lower()=="i" or direction.lower=="interact":

        if current_room == 0:
            print()
            print("There is nothing to interact with")
    #Entrance
        elif current_room == 1:
            print()
            print("Theres not much to interact with here.")
    #Regular food aisle
        elif current_room == 2:
            print()
            print("You search the cereal box,"
                  "you find a nice shiny key.")
            print("You put the key in your backpack")

    #cash registers
        elif current_room == 3:
            print()
            print("You open one of the cash registers, there is no cash.")

    #break room
        elif current_room == 4:
            if "Key" not in backpack:
                print()
                print("You try to open the door, it doesn't budge"
                      "there must be a key somewhere.")
            else:
                print("You unlock the door, do you want to enter? (y/n)")
                if direction.lower() == "y":
                    print("You enter the break room")
                else:
                    print("Okay")
        #frozen food aisle
        elif current_room == 5:
            print("It appears that derek is in here, do you wish to interact? (y/n)")
            if direction.lower() == "y" or direction.lower() == "yes":
                print("You approach derek he seems very aggressive, do you want to approach further?")
                if direction.lower() == "y" or direction.lower()=="yes":
                    print("You try to talk to derek, he immediately looks at you and kills you")
            else:
                print("Good choice.")
        #Deli
        elif current_room == 6:
            print()
            print("You reach over the counter and take a fresh piece of turkey")
            print("Do you want to eat it? (y/n)")
            if direction.lower()=="y" or direction.lower()=="yes":
                print("You consume the turkey, it was delicious")



    



    #Backpack
    elif direction.lower()=="b" or direction.lower()=="backpack":
        print(backpack)

    #Quit
    elif direction.lower()=="q" or direction.lower()=="quit":
        done = True

print("Thanks for playing!")
