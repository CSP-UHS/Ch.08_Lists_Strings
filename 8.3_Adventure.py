'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
room_list =[] #empty ray of room list

room = ["living room", 1, 2, 3, 4]

room.append(room_list)

current_room = 0

next_room = room_list[current_room][1]

done = False

while done == False:
    print("still going")
    print("")
    # print(room_list[current_room[0]])
    ans = input("What direction would you like to go N,E,W,S or Q for quit")

    if ans.lower == "q":
        done = True
    elif ans.lower == "n":
        print("You went north")
    if next_room == None:
        print("You cant fo that way")
    else:
        current_room == next_room



