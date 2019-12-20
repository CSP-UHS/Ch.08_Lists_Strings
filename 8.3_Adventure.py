'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''

roomList=[]
room={"You are standing on an old porch with broken boards beneath you. There is a swaying porch bench on the left side of you.\nThe front door is to the north of you. There are there different knockers on the door, each with a different symbol.\nThe first knocker is a skull, its dead eyes stare right through you. \nThe next is a pentagram, it's burning a hole through the door. \nIt's hot to the touch. The last knocker is...", 2, None, None, None}
roomList.append(room)
room={"You enter a room filled with dolls. There is a door to the north and to the west.", 4, 2, None, None}
roomList.append(room)
# room={" ", 5, 3, 0, 1}
# roomList.append(room)
room={"You  are in a room surrounded by clowns. There is a door to the north and to the west.", 6, None, None, 2}
roomList.append(room)
room={"You enter a room with a musty smell. Every where you look eyes of different creature follow you. \nOn th walls there are animals that have been shot down. In front of you there are three you must choose from. \nThe first is a black crow, its wings still spread out ready to fly. \nThe next animal is a black cat, its yellow eyes glowing in the darkness. \nThe last animal is the three headed dog, cerberus, that guards the gates to the underworld.", None, 5, 1, None}
roomList.append(room)
room={"Old Pictures ", 7, 6, 2, 4}
roomList.append(room)
room={"You are now in a poison room. A thick fog covers the floor below you. Shelves are filled with bottles of liquids of exhilarating colors.\nThere is a black table in the middle of the room. Three chalices are placed there, each filled with a unique concoction.\nThe first chalice has a purple drink with smoke overflowing from it. The second one is filled with a black drink and it gives you visions. \nThe last chalice is full of a red thick conjure. It reflects light off it but you hear voices as you get closer.", None, None, 3, 5}
roomList.append(room)
room={"The staircase takes you to a dungeon. There are cages with unholy creatures in them. \nWhat stands in front of you are three contraptions. ", 8, None, 5, None}
roomList.append(room)
room={"Out ", None, None, 7, None}
roomList.append(room)

# print("Travel through each room of the cursed house and choose wisely between three items. \nOne may just kill you on the spot while the other two will allow you to pass. \nDon't let your fear rise too high or you will not survive. Good Luck.")
fear=0
currentRoom=0
done=False
while not done:
    print()
    print(roomList[currentRoom][0])
    answer=str(input("What direction do you choose? north, south, east, west, q.quit"))
    if answer.lower()=="n" or answer.lower()=="north":
        nextRoom=roomList[currentRoom][1]
        if nextRoom==None:
            print("You can't go that way")
        else:
            currentRoom=nextRoom
    elif answer.lower()=="e" or answer.lower()=="east":
        nextRoom=roomList[currentRoom][2]
        if nextRoom==None:
            print("You can't go that way")
        else:
            currentRoom=nextRoom
    elif answer.lower()=="s" or answer.lower()=="south":
        nextRoom=roomList[currentRoom][3]
        # fear+=1
        if nextRoom==None:
            print("You can't go that way")
        else:
            currentRoom=nextRoom
    elif answer.lower()=="w" or answer.lower()=="west":
            nextRoom=roomList[currentRoom][4]
            if nextRoom==None:
                print("You can't go that way")
            else:
                currentRoom=nextRoom
    elif answer=="q" or answer=="quit":
        done=True

    print()
    print(roomList[currentRoom][1])
    answer=str(input("What direction do you choose?"))
    if answer.lower()=="n" or answer=="north":
        nextRoom=roomList[currentRoom][1]
        if nextRoom==None:
            print("You are unable to go that way")
        else:
            currentRoom=nextRoom
    elif answer.lower()=="e" or answer.lower()=="east":
        nextRoom=roomList[currentRoom][2]
        # fear+=1
        if nextRoom==None:
            print("You can't go that way")
        else:
            currentRoom=nextRoom
    if answer.lower()=="s" or answer.lower()=="south":
        nextRoom=roomList[currentRoom][3]
        if nextRoom==None:
            print("You can't go that way")
        else:
            currentRoom=nextRoom
    if answer.lower()=="w" or answer.lower()=="west":
        nextRoom=roomList[currentRoom][4]
        if nextRoom==None:
            print("You can't go that way")
        else:
            currentRoom=nextRoom

    print()
    print(roomList[currentRoom][2])
    answer=str(input("What direction do you choose? "))
    if answer.lower() == "n" or answer.lower() == "north":
        nextRoom = roomList[currentRoom][1]
        # fear+=1
        if nextRoom == None:
            print("You are unable to go that way")
        else:
            currentRoom = nextRoom
    elif answer.lower() == "e" or answer.lower() == "east":
        nextRoom=roomList[currentRoom][2]
        if nextRoom==None:
            print("You can't go that way")
        else:
            currentRoom=nextRoom
    elif answer.lower() == "s" or answer.lower() == "south":
        nextRoom=roomList[currentRoom][3]
        if nextRoom==None:
            print("You can't go there.")
        else:
            currentRoom=nextRoom
    elif answer.lower()=="w" or answer.lower()=="west":
        nextRoom=roomList[currentRoom][4]
        if nextRoom==None:
            print("you can't go that way")
        else:
            currentRoom=nextRoom

    print()
    print(roomList[currentRoom][3])
    answer=str(input("Which animal do you choose? a.crow b.black cat c.cerberus"))
    if answer.lower()=="n" or answer.lower()=="north":
        nextRoom = roomList[currentRoom][1]
        if nextRoom == None:
            print("you can't go that way")
        else:
            currentRoom = nextRoom
    elif answer.lower()=="e" or answer.lower()=="east":
        nextRoom=roomList[currentRoom][2]
        if nextRoom==None:
            print("You can't go that way")
        else:
            currentRoom=nextRoom
    elif answer.lower()=="s" or answer.lower()=="south":
        nextRoom = roomList[currentRoom][3]
        # fear += 1
        if nextRoom == None:
            print("You can't go there.")
        else:
            currentRom=nextRoom
    elif answer.lower()=="w" or answer.lower()=="west":
        nextRoom = roomList[currentRoom][4]
        if nextRoom == None:
            print("you can't go that way")
        else:
            currentRoom = nextRoom
    print()
    print(roomList[currentRoom][4])
    answer = str(input("What direction do you choose?"))
    if answer.lower() == "n" or answer.lower() == "north":
        nextRoom = roomList[currentRoom][1]
        if nextRoom == None:
            print("you can't go that way")
        else:
            currentRoom = nextRoom
    elif answer.lower() == "e" or answer.lower() == "east":
        nextRoom = roomList[currentRoom][2]
        if nextRoom == None:
            print("You can't go that way")
        else:
            currentRoom = nextRoom
    elif answer.lower() == "s" or answer.lower() == "south":
        nextRoom = roomList[currentRoom][3]
        # fear += 1
        if nextRoom == None:
            print("You can't go there.")
        else:
            currentRoom=nextRoom
    elif answer.lower() == "w" or answer.lower() == "west":
        nextRoom = roomList[currentRoom][4]
        if nextRoom == None:
            print("you can't go that way")
        else:
            currentRoom = nextRoom

    print()
    print(roomList[currentRoom][5])
    answer=str(input("What direction do you choose?"))
    if answer.lower()=="n" or answer.lower()=="north":
        nextRoom=roomList[currentRoom][1]
        if nextRoom==None:
            print("You can't go there.")
        else:
            currentRoom=nextRoom
    elif answer.lower()=="e" or answer.lower()=="east":
        nextRoom=roomList[currentRoom][2]
        # fear+=1
        if nextRoom==None:
            print("You can't go that way.")
        else:
            currentRoom=nextRoom
    elif answer.lower()=="s" or answer.lower()=="south":
        nextRoom=roomList[currentRoom][3]
        if nextRoom==None:
            print("You can't go that way")
        else:
            currentRoom=nextRoom
    elif answer.lower()=="w" or answer.lower()=="west":
        nextRoom=roomList[currentRoom][4]
        if nextRoom==None:
            print("You can't go that way")
        else:
            currentRoom=nextRoom
    print()
    print(roomList[currentRoom][6])
    answer=str(input("What direction do you choose?"))
    if answer.lower()=="n" or answer.lower()=="north":
        nextRoom=roomList[currentRoom][1]
        if nextRoom==None:
            print("You can't go there.")
        else:
            currentRoom=nextRoom
    elif answer.lower()=="e" or answer.lower()=="east":
        nextRoom = roomList[currentRoom][2]
        if nextRoom == None:
            print("You can't go there.")
        else:
            currentRoom = nextRoom
    elif answer.lower()=="s" or answer.lower()=="south":
        nextRoom = roomList[currentRoom][3]
        # fear+=1
        if nextRoom==None:
            print("You can't go there.")
        else:
            currentRoom = nextRoom
    elif answer.lower()=="w" or answer.lower()=="west":
        nextRoom = roomList[currentRoom][1]
        if nextRoom == None:
            print("You can't go there.")
        else:
            currentRoom = nextRoom

    print()
    print(roomList[currentRoom][7])
    # if done=False and fear<5:
    #     print("You escaped the haunted house, congrats! ")
    # else:
    #     print("You managed to get to the door but ")
    # if fear>6:
    #     done=True
    # elif fear>3:
    #     print("Your fear level is rising choose your items carefully")
    # if currentRoom>4:
    #     print("You are almost there")
