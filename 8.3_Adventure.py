'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
# Loading all rooms
room_list = []
room = ["You are in the Hospital Entrance. You're excited to start your day at the hospital and see doctors coming in "
        "behind you.", None, 1, None, None]  # description of room, then rooms around it north, east, south, and west
room_list.append(room)
room = ["You are in the Emergency Room. It already seems pretty busy, which makes you anxious but you're ready to save "
        "lives.", 2, 6, 3, 0]
room_list.append(room)
room = ["You are in the Staff Room. You see a few Residents and Interns eating snacks and taking breaks.", None, 7, 1,
        None]
room_list.append(room)
room = ["You are in the Trauma Center. You notice your third patient and know it'll be your hardest one. "
        "\n Make sure you're ready before attempting this one.", 1, 5, 4, None]
room_list.append(room)
room = ["You are in the Supply Closet. You can hear someone rustling around in the "
        "back and realize you don't need to be in here.", 3, None, None, None]
room_list.append(room)
room = ["You are in the Pediatrics Room. You hear lot of kids around and can't help but smile."
        "\n You notice your first patient in a nearby room.", 6, None, None, 3]
room_list.append(room)
room = ["You are in the Oncology Unit. The air here feels a bit different and you see a few people sitting "
        "in chairs during chemo treatments. \n You see your second patient waiting for radiation.", 7, 8, 5, 1]
room_list.append(room)
room = ["You are in the Restroom. You hear a toilet flush and something kind of stinks.", None, None, 6, 2]
room_list.append(room)
room = ["You are in the Operating Room. You get nervous and excited, feeling some adrenaline pump in your veins."
        "You can't wait to hopefully be a surgeon someday.", None, None, None, 6]
room_list.append(room)

# spawning player
current_room = 0

done = False
p1 = False
p2 = False
p3 = False

moves = 150
sleep = 100
print("Welcome to the Hospital Adventure Game.")
print(" ")
print("In this game you are a new Intern, you must complete all of your tasks before the end of the day.")
print("If you don't complete your tasks within 150 moves, you'll be kicked out. "
      "\nIf one of your patients die, you will also be kicked "
      "out.")
print("Lastly, you have needs just like any other person. Make sure you take care of these or you'll also be kicked "
      "out.")
print("Use NESW to move to different rooms, Q to quit, C to show your clipboard, and A to show actions you can perform.")
while not done:
    print(" ")
    print(room_list[current_room][0])
    direction = input("Where would you like to go? NESW (C, A, Q)")
    if direction.lower() == "n" or direction.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room is None:
            print("You can't go that way.")
            moves -= 1
            sleep -= 2
        else:
            current_room = next_room
    if direction.lower() == "e" or direction.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room is None:
            print("You can't go that way.")
            moves -= 1
            sleep -= 2
        else:
            current_room = next_room
    if direction.lower() == "s" or direction.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room is None:
            print("You can't go that way.")
            moves -= 1
            sleep -= 2
        else:
            current_room = next_room
    if direction.lower() == "w" or direction.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room is None:
            print("You can't go that way.")
            moves -= 1
            sleep -= 2
        else:
            current_room = next_room
    if direction.lower() == "q" or direction.lower() == "quit":
        print("You quit, hope you had fun!")
        done = True
    if direction.lower() == "c" or direction.lower() == "clipboard":
        if not p1:
            print("Patient 1: Pediatrics Room. Checkup.")
        if not p2:
            print("Patient 2: Oncology Unit. Radiation.")
        if not p3:
            print("Patient 3: Trauma Center. Big trauma, will be surgical.")
        else:
            print("Congrats you won!")
            done = True
