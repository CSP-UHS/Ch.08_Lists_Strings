'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''

roomList=[]
room={"You are standing on an old porch with broken boards beneath you. There is a swaying porch bench on the left side of you."
      "The front door is to the north of you. There are there different knockers on the door, each with a different symbol."
      "The first knocker is a skull, its dead eyes stare right through you. "
      "The next is a pentagram, it's burning a hole through the door. "
      "It's hot to the touch. The last knocker is...", 2, None, None, None}
roomList.append(room)
room={"You enter a room filled with dolls. There is a door to the north and to the west.", 4, 2, None, None}
roomList.append(room)
# room={" ", 5, 3, 0, 1}
# roomList.append(room)
room={"You  are in a room surrounded by clowns. There is a door to the north and to the west.", 6, None, None, 2}
roomList.append(room)
room={"You enter a room with a musty smell. Every where you look eyes of different creature follow you. "
      "On th walls there are animals that have been shot down. In front of you there are three you must choose from. "
      "The first is a black crow, its wings still spread out ready to fly. "
      "The next animal is a black cat, its yellow eyes glowing in the darkness. "
      "The last animal is the three headed dog, cerberus, that guards the gates to the underworld.", None, 5, 1, None}
roomList.append(room)
room={"Old Pictures ", 7, 6, 2, 4}
roomList.append(room)
room={"You are now in a poison room. A thick fog covers the floor below you. Shelves are filled with bottles of liquids of exhilarating colors."
      "There is a black table in the middle of the room. Three chalices are placed there, each filled with a unique concoction."
      "The first chalice has a purple drink with smoke overflowing from it. The second one is filled with a black drink and it gives you visions."
      "The last chalice is full of a red thick conjure. It reflects light off it but you hear voices as you get closer.", None, None, 3, 5}
roomList.append(room)
room={"The staircase takes you to a dungeon. There are cages with unholy creatures in them."
      "What stands in front of you are three contraptions. ", 8, None, 5, None}
roomList.append(room)
room={"Out ", None, None, 7, None}
roomList.append(room)

print("Travel through each room of the cursed house and choose wisely between three items. "
      "One may just kill you on the spot while the other two will allow you to pass. "
      "Don't let your fear rise too high or you will not survive. Good Luck.")
fear=0
currentRoom=0
done=False
while not done:
    print()
    print(roomList[currentRoom][0])
    answer=str(input("What knocker do you choose? a.skull b.pentagram c. q.quit"))
    if answer=="a" or answer=="skull":
        print("The knocker is cold to the touch, Its eyes begin to glow and the floor beneath you decays.  ")
        done=True
    elif answer=="b" or answer=="pentagram":
        print("The know bursts into flame in front of you, your face burns from the heat. Your path is now open and you may enter the house.")
        nextRoom=roomList[currentRoom][1]
        if nextRoom==None:
            print("You can't go that way")
        else:
            currentRoom=nextRoom
    elif answer=="c" or answer=="":
        nextRoom=roomList[currentRoom][1]
        fear+=1
        if nextRoom==None:
            print("You can't go that way")
        else:
            currentRoom=nextRoom
    # elif answer=="W" or answer=="west":
        #     nextRoom=roomList[currentRoom][2]
        #     if nextRoom==None:
        #         print("You can't go that way")
        #     else:
        #         currentRoom=nextRoom
    elif answer=="q" or answer=="quit":
        done=True
    print()
    print(roomList[currentRoom][1])
    answer=str(input("Which doll do you choose? a.the bassinet b.the crib c.the carriage"))
    if answer=="a" or answer=="the bassinet":
        nextRoom=roomList[currentRoom][2]
        if nextRoom==None:
            print("You are unable to go that way")
        else:
            currentRoom=nextRoom
    elif answer=="b" or answer=="the crib":
        nextRoom=roomList[currentRoom][2]
        fear+=1
        if nextRoom==None:
            print("You can't go that way")
        else:
            currentRoom=nextRoom
    if answer=="c" or answer=="the carriage":
        # print(" ")
        done=True
    print()
    print(roomList[currentRoom][2])
    answer=str(input("Which clown do you choose? a. b. c. "))
    if answer == "a" or answer == " ":
        nextRoom = roomList[currentRoom][3]
        fear+=1
        if nextRoom == None:
            print("You are unable to go that way")
        else:
            currentRoom = nextRoom
    elif answer == "b" or answer == "the crib":
        # print(" ")
        done=True
    if answer == "c" or answer == "the carriage":
        nextRoom=roomList[currentRoom][3]
        if nextRoom==None:
            print("You can't go there.")
        else:
            currentRoom=nextRoom
    print()
    print(roomList[currentRoom][3])
    answer=str(input("Which animal do you choose? a.crow b.black cat c.cerberus"))
    if answer=="a" or answer=="crow":
        # print(" ")
        done=True
    elif answer=="b" or answer=="black cat":
        nextRoom=roomList[currentRoom][4]
        if nextRoom==None:
            print(" ")
        else:
            currentRoom=nextRoom
    elif answer=="c" or answer=="cerberus":
        nextRoom = roomList[currentRoom][3]
        fear += 1
        if nextRoom == None:
            print("You can't go there.")
        else:
            currentRoom=nextRoom

    print()
    print(roomList[currentRoom][5])
    answer=str(input("Which poison do you choose? a.purple b.black c.red"))
    if answer=="a" or answer=="purple":
        # print(" ")
        nextRoom=roomList[currentRoom][6]
        if nextRoom==None:
            print("You can't go there.")
        else:
            currentRoom=nextRoom
    elif answer=="b" or answer=="black":
        # print(" ")
        nextRoom=roomList[currentRoom][6]
        fear+=1
        if nextRoom==None:
            print("You can't go there.")
        else:
            currentRoom=nextRoom
    elif answer=="c" or answer=="red":
        # print(" ")
        done=True
    print()
    print(roomList[currentRoom][6])
    answer=str(input("What contraption do you choose? a.guillotine b.stretch c.noose"))
    if answer=="a" or answer=="guillotine":
        # print(" ")
        nextRoom=roomList[currentRoom][7]
        if nextRoom==None:
            print("You can't go there.")
        else:
            currentRoom=nextRoom
    elif answer=="b" or answer=="stretch":
        # print(" ")
        done=True
    elif answer=="c" or answer=="noose":
        # print(" ")
        nextRoom = roomList[currentRoom][7]
        fear+=1
        if nextRoom==None:
            print("You can't go there.")
        else:
            currentRoom = nextRoom
    print()
    print(roomList[currentRoom][7])
    # if done=False and fear<5:
    #     print("You escaped the haunted house, congrats! ")
    # else:
    #     print("You managed to get to the door but ")
    if fear>6:
        done=True
    elif fear>3:
        print("Your fear level is rising choose your items carefully")
    if currentRoom>4:
        print("You are almost there")
