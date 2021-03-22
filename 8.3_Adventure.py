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
import random
done = False
p1 = False
p2 = False
p3 = False
egg = 0
roll = False
surgery = 0
moves = 100
sleep = 50
print("Welcome to the Hospital Adventure Game.")
print(" ")
print("In this game you are a new Intern, you must complete all of your tasks before the end of the day.")
print("If you don't complete your tasks within 100 moves, you'll be kicked out. "
      "\nIf one of your patients die, you will also be kicked "
      "out.")
print("Lastly, you have needs just like any other person. Make sure you take care of these or you'll also be kicked "
      "out.")
print("Use NESW to move to different rooms, Q to quit, C to show your clipboard, and A to show actions you can perform.")
while not done:
    print(" ")
    print(room_list[current_room][0])
    direction = input("Where would you like to go? NESW (C, A, Q)") # input question at the start of every move
    if direction.lower() == "n" or direction.lower() == "north": # if user puts this in the move this direction
        next_room = room_list[current_room][1]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room
            moves -= 1
            sleep -= 2
    if direction.lower() == "e" or direction.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room
            moves -= 1
            sleep -= 2
    if direction.lower() == "s" or direction.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room
            moves -= 1
            sleep -= 2
    if direction.lower() == "w" or direction.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room is None:
            print("You can't go that way.")
        else:
            current_room = next_room
            moves -= 1
            sleep -= 2
    if direction.lower() == "q" or direction.lower() == "quit": # ends the game
        print("You quit, hope you had fun!")
        done = True
    if direction.lower() == "c" or direction.lower() == "clipboard": # shows player what they need to complete
        if not p1:
            print("Patient 1: Pediatrics Room. Checkup.")
        if not p2:
            print("Patient 2: Oncology Unit. Radiation.")
        if not p3:
            print("Patient 3: Trauma Center. Big trauma, will be surgical.")
        else:
            print("Congrats you won!")
            done = True
    if sleep == 25: # warns player about sleep getting low
        print("You're getting tired. Head to the staff room to take care of yourself!")
    if sleep == 0:
        print("You passed out from not taking care of your needs. You were kicked out.")
        done = True
    if moves == 50: # warns player about moves getting low
        print("You only have 50 moves left!")
    if moves == 25:
        print("You only have 25 moves left!")
    if moves == 10:
        print("You only have 10 moves left, better be careful how you spend them!")
    if moves == 0:
        print("You ran out of moves and got kicked out for not helping your patients in time.")
        done = True
    if direction.lower() == "a" or direction.lower() == "action": # actions players can do in certain rooms
        moves -= 1
        sleep -= 2
        if current_room == 0:
            print("There isn't much you can do here, try going to a different area for actions.")
            moves +=1
            sleep +=2
        if current_room == 1:
            print("You ask around to see if anyone needs help but remember you need to focus on your patients.")
            moves += 1
            sleep += 2
        if current_room == 2:
            if roll: # if the player is rolling patient 3 to the operating room and go here they went off path and kil the patient
                print("You didn't take the most direct path and your patient died!")
                done = True # game ends
            room2 = input("You see a bed you can rest on, would you like to rest? (Y for yes, N for no)")
            if room2.lower() == "y" or room2.lower() == "yes":
                print("You fully rest, but lose 10 moves.") # player regains all sleep but loses 10 moves
                sleep = 50
                moves -= 10
            if room2.lower() == "n" or room2.lower() == "no":
                print("You decide not to sleep.")
                moves += 1
                sleep += 2
            else:
                print("That isn't an option.") # player input a non-valid option
                moves += 1
                sleep += 2
        if current_room == 3:
            room3 = input("The doctors around you ask you to help roll this patient to the operating room. "
                          "Would you like to do this now? (Y for yes, N for no)")
            if room3.lower() == "y" or room3.lower() == "yes": # will start quest for patient 3
                print("You decide to roll the patient to the operating room. Be sure to go on the "
                      "most direct path or they may bleed out.")
                roll = True
            if room3.lower() == "n" or room3.lower() == "no":
                print("You decide to come back later.")
                moves += 1
                sleep += 2
            else:
                print("That isn't an option.")
                moves += 1
                sleep += 2
        if current_room == 4:
            if roll: # same as room 2
                print("You didn't take the most direct path and your patient died!")
                done = True
            egg = random.randint (1, 55) # picks random number 1-55
            if egg == 54 or egg == 32 or egg == 7: # if one of these numbers they get a special prize
                print("Congrats you found an easter egg in the game and your needs were fully restored. You also gained 20 moves!")
                sleep = 50
                moves += 20
            else: # if it wasn't one of the three nothing happens
                print("Hmm.. nothing here.")
        if current_room == 5:

        if current_room == 6:

        if current_room == 7:
            if roll: # same as room 2 and 4
                print("You didn't take the most direct path and your patient died!")
                done = True
            if not roll:
                print("Something in here smells terrible, you realize you want to get out of here as soon as possible.")
        if current_room == 8:
            if roll:
                print("Good job! You made it to the Operating room. During the "
                      "surgery a surgeon lets you step in to do a few steps.")
                surgery = random.randint(1,50) # picks random number 1-50
                if surgery == 43 or surgery == 3: # if one of these then the patient dies
                    print("You made the wrong cut during surgery and your patient died!")
                    done = True
                else: # if they didn't get one of the two numbers the surgery goes well
                    print("Phew! You successfully did those surgical steps and patient 3 lives!")
                    p3 = True
        if p1 == True and p2 == True and p3 == True: # if the player completes all the tasks for the patients they win
            print("Congrats you have helped all your patients! You win!")
            done = True
