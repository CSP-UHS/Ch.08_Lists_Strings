'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
room0 = []
room1 = []
room2 = []
room3 = []
room4 = []
room5 = []
room6 = []
room7 = []
room8 = []
room9 = []
CR = []
r = 1
key = "false"
done = "false"
dire = 0
none = 0
inside = 1
room_list = []

for x in range(10000):
    room0 = ["You are standing on an old rickety porch", room1, none, none, none]  # Room0
    room_list.append(room0)
    room1 = ["You walk into a large entrance wih chairs and tables covered in dust strewn about.", room4, room3, room0, room2]  # Room1
    room_list.append(room1)
    room2 = ["Empty chairs and a broken sofa lie in the middle of what as a living room", none, room1, none, none]  # Room2
    room_list.append(room2)
    room3 = ["It's a kitchen with pots and pans all over the place. There's water all over the floor.", none, none, none, room1]  # Room3
    room_list.append(room3)
    room4 = ["You see a long, dark hallway with two broken doors at either sides of you.", room5, room7, room1, room6]  # Room4
    room_list.append(room4)
    room5 = ["You walk further into the hallway, reaching two doors at your sides and one at the very end.", room1, room9, room4, room8]  # Room5
    room_list.append(room5)
    room6 = ["There are shelves lining the walls with small scraps of food on them, looks like a pantry", room8, room4, none, none]  # Room6
    room_list.append(room6)
    room7 = ["It's a dirty bathroom with a shattered toilet and a faucet slowly dripping water", room9, none, none, room4]  # Room7
    room_list.append(room7)
    room8 = ["You enter a bedroom with two beds on either side of the room", none, room5, room6, none]  # Room8
    room_list.append(room8)
    room9 = ["There's a large bed in the corner of the room with some liquid leaking from the ceiling", none, none, room7, room5]  # Room9
    room_list.append(room9)
CR = room0
print(room0[0])
while done == "false":
    dire = input("where would you like to go? (N)orth (E)ast (S)outh (W)est (Q)uit")  # Directions
    print()
    if dire == "N" or dire == "n":
        if CR[1] == none:
            print("you can't go that way")
        else:
            CR = CR[1]
            print(CR[0])
    elif dire == "E" or dire == "e":
        if CR[2] == none:
            print("You can't go that way")
        else:
            CR = CR[2]
            print(CR[0])
    elif dire == "S" or dire == "s":
        if CR[3] == none:
            print("You can't go that way")
        elif CR[3] == room6 and key == "false":
            print("The door is locked")
        else:
            CR = CR[3]
            print(CR[0])
    elif dire == "W" or dire == "w":
        if CR[4] == none:
            print("You can't go that way")
        else:
            CR = CR[4]
            print(CR[0])
    elif dire == "Q" or dire == "q":
        done = "true"
        print("Farewell")
    else:
        print("I don't understand")
'''
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
'''
