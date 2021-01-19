'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import random

room_list = []
#0 - Entrance
room = ["You are in the Entrance. It's a skinny room, but filled with people, you will have to do some maneuvering.",None,1,None,None]
room_list.append(room)
#1 - Central Dining
room = ["You are in the main dining room, a large and open space from your rat perspective. \nMany people eating at their tables, but you can't quite see what they're eating. \nTo your left you see stairs going up somewhere, and in directly ahead you see a kitchen, but no entrance.",6,2,None,0]
room_list.append(room)
#2 - North Dining
room = ["You are in the second dining room, a space similar to the main dining room, but a bit more secluded. \nThere is a door to the kitchen in front of you.",3,None,None,1]
room_list.append(room)
#3 - Kitchen
room = ["You are in the kitchen. Chefs everywhere. One of them almost steps on you as they busily walk by. \nYou look to see what they're carrying, but there's nothing interesting.",5,4,2,None]
room_list.append(room)
#4 - Fridge
room = ["You are in the walk-in fridge. It's pretty cold, so you shouldn't stay long. \nYou see another rat with some cheese. \nIt's not the good cheese though. There's food everywhere, you almost don't know where to start.",None,None,None,3]
room_list.append(room)
#5 - Storage
room = ["You are in the walk-in pantry. It's a ratty little room. \nThere's some good stuff in there, but there doesn't seem to be any cheese.",None,None,3,None]
room_list.append(room)
#6 - Balcony
room = ["You pry open the vent with your fork and slip through the grate. \nAs you are walking up the stairs, however, a woman screams and runs through the door. \nYou listen closely for what she says, and sure enough, she ratted you out to the authorities. \nYou can't go back down or you'll get caught, and the balcony is isolated...",None,None,None,None]
room_list.append(room)
current_room = 0
#Instructions
print()
print("---------------------------------------------------------------------------------------------------------------")
print()
print("Welcome to the game. You are a rat attempting to recover some cheese from a nearby pizza restaurant.")
print("This is no ordinary cheese, and it's very rare. You heard stirrings in the rat community that there might be")
print("a piece here. You haven't eaten in a long time, so this mission is crucial.")
print()
print("You will navigate from room to room, trying to find this coveted piece of cheese. Good luck.")
print()
print("In any room, you can conduct a search to see what you find.")
print("---------------------------------------------------------------------------------------------------------------")


cheese = False
fork = False
done = False
spotted = 0
while done == False:

    print()
    print(room_list[current_room][0])
    print()
    choice = input("What would you like to do? ((N)orth, (E)ast, (S)outh, (W)est, (F)orage, (Q)uit)")
    spotted = random.randrange(0,20)
    if choice.upper() == "N" or choice.upper() == "NORTH":
        next_room = room_list[current_room][1]
        if next_room == None:
            print()
            print("You can't go that way!")
        elif next_room == 6 and fork == False:
            print()
            print("You go up to the balcony door, but there seems to be no way for you to open it. \nThere is a vent next to the door. \nIf only you had a kitchen utensil or something to pry it open.")
        elif next_room == 6 and fork == True:
            current_room = next_room
        else:
            current_room = next_room
    elif choice.upper() == "E" or choice.upper() == "EAST":
       next_room = room_list[current_room][2]
       if next_room == None:
           print()
           print("You can't go that way!")
       else:
           current_room = next_room
    elif choice.upper() == "S" or choice.upper() == "SOUTH":
        next_room = room_list[current_room][3]
        if next_room == None:
            print()
            print("You can't go that way!")
        else:
            current_room = next_room
    elif choice.upper() == "W" or choice.upper() == "WEST":
        next_room = room_list[current_room][4]
        if next_room == None:
            print()
            print("You can't go that way!")
        else:
            current_room = next_room
    elif choice.upper() == "F" or choice.upper() == "FORAGE":
        if current_room == 0:
            print("\nYou don't find anything, and you probably shouldn't be looking around with so many people present.")
        elif current_room == 1:
            print("\nYou find a scrap of bread. It'll tide you over, but it's not what you're looking for.")
        elif current_room == 2:
            print("\nYou find another rat, presumably doing what you're doing. He says that there's some cheese in the fridge, \nbut it might not be the right variety. The only other place it could be is on the balcony, he says. \nHe seems a little suspicous, so whether you believe him or not is your choice. \nIt might be a trap.")
        elif current_room == 3:
            print("\nIn your foraging, you almost step on a rat trap. Close call.")
        elif current_room == 4:
            if fork == False:
                print("\nYou search high and low for the cheese you need, but to no avail. \nMaybe that other rat took the last of it. \nYou find a fork in the corner. You take it with you.")
                fork = True
            else:
                print("Nothing new.")
        elif current_room == 5:
            print("\nYou don't find any food that resembles cheese. You wonder why you're even in here.")
        elif current_room == 6:
            choice = input("\nIn the corner, you see it. The cheese you have been looking for. You run over and pick it up. \nBut there's nowhere to go, the stairs are blocked, and it's a long drop everywhere else. \nYou have your cheese, but do you jump ((Y)es or (N)o)?")
            if choice.upper() == "Y" or choice.upper() == "YES":
                print("In a leap of faith, you jump off the balconoy with the cheese in your mouth. Because you're a rat, you land with little impact. \nYou successfully completed the mission. \n\nYOU WIN!")
                done = True
            else:
                print("You decide not to jump. In your hesitation, the restaurant staff capture you. It's the end of the line. \n\nGAME OVER")
                done = True
    elif choice.upper() == "Q" or choice.upper() == "QUIT":
        print()
        print("Exiting game...")
        done = True
    if spotted == 19:
        print("\nYou've been spotted! The employees throw you out, but you can get back in easily. \nYou return to where you started.")
        if fork == True:
            print("They are letting you keep the fork.")
        current_room = 0





