'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
room_lists = []

room = ["You are in Bedroom 2, the door is lock,in the room there is a metal bat that you can use it to break and go to the next room", 1, 6, None, None]
room_lists.append(room)
room = ["You have broke the lock and now ou are in Bedroom 1 on the table there is a number it look like a passcode of sort and there is a safe box", None, 2, 0, None]
room_lists.append(room)
room = ["You are in North Hall, the wall of the hall is all white with no chair or table on sight", 3, 4, 6, 1]
room_lists.append(room)
room = ["You are in the balcony, there is nothing as far as the eye can see, no tree or anything, it look like apace", None, None, 2, None]
room_lists.append(room)
room = ["You are in the Kitchen, there is a robot machine cooking food and in the right conner there is a humanoid robot standing", None, None, 5, 2]
room_lists.append(room)
room = ["Dining Room, there is one table and three chair, and on the table there is a steaming hot meal, it look like someone was here not long ago", 4, None, None, 6]
room_lists.append(room)
room = ["South hall, the hall look like a normal hall but on the wall there is a word and it look like your name, the hall is a little bit messy it look like someone was fighting here", 2, 5, 7, 0]
room_lists.append(room)
room = ["porch, there is nothing special about the porch except there is a wall but no door, it look like a teleportation room, on the right side there is a computer and on the computer there is a 3D picture of earth", 6, None, None, None]
room_lists.append(room)
#  this code make sure that we are in the first room
current_room = 0

done = False

while not done:
    print()
    print(room_lists[current_room][0])
#   this code ask the user what direction they want to go
    user_ans = input("N,E,W,S or Q:  ")
#   this code look and see what the user chose as their direction
    if user_ans.lower() == 'n' or user_ans.lower() == 'north':
        next_room = room_lists[current_room][1]
#   this code look to see if the user can go at that direction or not
        if next_room is None:
            print("You can't go that way")
        else:
            current_room = next_room
    if user_ans.lower() == 'e' or user_ans.lower() == 'east':
        next_room = room_lists[current_room][2]

        if next_room is None:
            print("You can't go that way")
        else:
            current_room = next_room
    if user_ans.lower() == 's' or user_ans.lower() == 'south':
        next_room = room_lists[current_room][3]

        if next_room is None:
            print("You can't go that way")
        else:
            current_room = next_room
    if user_ans.lower() == 'w' or user_ans.lower() == 'west':
        next_room = room_lists[current_room][4]

        if next_room is None:
            print("You can't go that way")
        else:
            current_room = next_room
#   this code make sure the code loop stop when the user want to quit
    game_quit = "q"
    if user_ans.lower() == "q" or user_ans.lower() == "quit":
        done = True

