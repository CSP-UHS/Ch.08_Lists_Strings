'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''

CR = []
r = 1
done = "false"
dire = 0
none = 10
inside = 1
room_list = []


room0 = ["You are standing on an old rickety porch", 1, none, none, none]  # Room0
room_list.append(room0)
room1 = ["You walk into a large entrance wih chairs and tables covered in dust strewn about.", 4, 3, 0, 2]  # Room1
room_list.append(room1)
room2 = ["Empty chairs and a broken sofa lie in the middle of what as a living room", none, 1, none, none]  # Room2
room_list.append(room2)
room3 = ["It's a kitchen with pots and pans all over the place. There's water all over the floor.", none, none, none, 1]  # Room3
room_list.append(room3)
room4 = ["You see a long, dark hallway with two broken doors at either sides of you.", 5, 7, 1, 6]  # Room4
room_list.append(room4)
room5 = ["You walk further into the hallway, reaching two doors at your sides and one at the very end.", 1, 9, 4, 8]  # Room5
room_list.append(room5)
room6 = ["There are shelves lining the walls with small scraps of food on them, looks like a pantry", 8, 4, none, none]  # Room6
room_list.append(room6)
room7 = ["It's a dirty bathroom with a shattered toilet and a faucet slowly dripping water", 9, none, none, 4]  # Room7
room_list.append(room7)
room8 = ["You enter a bedroom with two beds on either side of the room", none, 5, 6, none]  # Room8
room_list.append(room8)
room9 = ["There's a large bed in the corner of the room with some liquid leaking from the ceiling", none, none, 7, 5]  # Room9
room_list.append(room9)

CR = room_list[0]
print(CR[0])

while done == "false":
    dire = input("where would you like to go? (N)orth (E)ast (S)outh (W)est (Q)uit")  # Directions
    print()
    if dire == "N" or dire == "n":  # North
        if CR[1] == 10:
            print("you can't go that way")
        else:
            CR = room_list[CR[1]]
            print(CR[0])
    elif dire == "E" or dire == "e":  # East
        if CR[2] == 10:
            print("You can't go that way")
        else:
            CR = room_list[CR[2]]
            print(CR[0])
    elif dire == "S" or dire == "s":  # South
        if CR[3] == 10:
            print("You can't go that way")
        else:
            CR = room_list[CR[3]]
            print(CR[0])
    elif dire == "W" or dire == "w":  # West
        if CR[4] == 10:
            print("You can't go that way")
        else:
            CR = room_list[CR[4]]
            print(CR[0])
    elif dire == "Q" or dire == "q":  # Quit
        done = "true"
        print("Farewell")
    else:
        print("I don't understand")
