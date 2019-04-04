'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
done = "false"
dire = 0
none = 0
inside = 1
room_list = []
room0 = ["You are standing on an old rickety porch", 1, none, none, none]
room_list.append(room0)
room1 = ["You walk into a large entrance wih chairs and tables covered in dust strewn about.", 1, 2, 3, 4]
room_list.append(room1)
room2 = ["Empty chairs and a broken sofa lie in the middle of what as a living room", none, 2, none, none]
room_list.append(room2)
room3 = ["It's a kitchen with pots and pans all over the place. There's water all over the floor.", none, none, none, 4]
room_list.append(room3)
room4 = ["You see a long, dark hallway with two broken doors at either sides of you.", 1, 2, 3, 4]
room_list.append(room4)
room5 = ["You walk further into the hallway, reaching two doors at your sides and one at the very end.", 1, 2, 3, 4]
room_list.append(room5)
room6 = ["There are shelves lining the walls with small scraps of food on them, looks like a pantry", 1, 2, none, none]
room_list.append(room6)
room7 = ["It's a dirty bathroom with a shattered toilet and a faucet slowly dripping water", 1, none, none, 4]
room_list.append(room7)
room8 = ["You enter a bedroom with two beds on either side of the room", none, 2, 3, none]
room_list.append(room8)
room9 = ["There's a large bed in the corner of the room with some liquid leaking from the ceiling", none, none, 3, 4]
room_list.append(room9)
print(room0[0])
C_R = room0
while done == "false":
    print(C_R[0])
    dire = input("where would you like to go? (N)orth (E)ast (S)outh (W)est (Q)uit")
    if C_R == room0:
        if  dire == "N" or dire == "n":
            C_R = room1
        elif dire == "E" or dire == "e" or dire == "W" or dire == "w" or dire == "S" or dire == "s":
            print("You aren't physically able to move in those direction")
        else:
            print("You can't do that")
    elif C_R == room1:

    elif C_R == room2:

    elif C_R == room3:

    elif C_R == room4:

    elif C_R == room5:

    elif C_R == room6:

    elif C_R == room7:

    elif C_R == room8:

    elif C_R == room9:

