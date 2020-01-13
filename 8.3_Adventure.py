'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
print() #introduction/directions
print("Welcome to the Escape House! The only way that you can escape is through the back living room.")
print("In order to leave the house, you must have a key. It is hidden in one of 8 rooms in the house.")
print()
print("Be careful during your adventure as searching for the key is dangerous.")
print("You must enter through the porch and use the key to exit the living room in order to win!")
print()
print("There is a family in the house. If you are caught by the parents or a child, you lose!")
print()
print("Good luck escaping!")

room_list=[] #name of rooms
room=["You enter the porch. There is nothing there to search for.",2,None,None,None]
room_list.append(room)
room=["You enter the dining room.",4,2,None,None]
room_list.append(room)
room=["You enter the kitchen.",5,3,0,1]
room_list.append(room)
room=["You enter the office.",6,None,None,2]
room_list.append(room)
room=["You enter the master bedroom.",None,5,1,None]
room_list.append(room)
room=["You enter the bathroom.",7,6,2,4]
room_list.append(room)
room=["You enter the guest room.",None,None,3,5]
room_list.append(room)
room=["You enter the living room.",None,None,5,None]
room_list.append(room)

key_found = 0

current_room = 0
done = False
while not done:
    print()
    print(room_list[current_room][0])
    user_Input = input("Where would you like to go next? North, East, South, West, or Quit? ")
    if user_Input.upper() == "N" or user_Input.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("Sorry, You can't go that way.")
        else:
            current_room = next_room
    elif user_Input.upper() == "E" or user_Input.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("Sorry, You can't go that way.")
        else:
            current_room = next_room
    elif user_Input.upper() == "S" or user_Input.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("Sorry, You can't go that way.")
        else:
            current_room = next_room
    elif user_Input.upper() == "W" or user_Input.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("Sorry, You can't go that way.")
        else:
            current_room = next_room
    elif user_Input.upper() == "Q" or user_Input.lower() == "quit":
        done = True
    else:
        print("I do not understand.")
    if current_room == 1:
        search = input("Would you like to search the dining room? ")
        print()
        if search.upper() == "Y" or search.upper() == "YES":
            print("You found a tablecloth, but there is no key under it.")
            print("You found a couple of old plates, but no key. Keep looking around!")
            print()
    if current_room == 2:
        search = input("Would you like to search the kitchen? ")
        print()
        if search.upper() == "Y" or search.upper() == "YES":
            print("All of the appliances are locked. There is also nothing under them.")
            print("You should look somewhere else!")
            print()
    if current_room == 3:
        search = input("Would you like to search the office? ")
        print()
        if search.upper() == "Y" or search.upper() == "YES":
            print("You found a key, but it is not the right one. Keep searching!")
            print()
    if current_room == 4:
        search = input("Would you like to search the master bedroom? ")
        print()
        if search.upper() == "Y" or search.upper() == "YES":
            print("Sorry, you were caught by the father while you were searching.")
            print("Better luck next time!")
            print()
            done = True
    if current_room == 5:
        search = input("Would you like to search the bathroom? ")
        print()
        if search.upper() == "Y" or search.upper() == "YES":
            print("You found something behind the mirror. It's an escape route!")
            escape = input("Would you like to escape the house? ")
            print()
            if escape.upper() == "Y" or escape.upper() == "YES":
                print("Sorry, the 4 year-old child found you. He told his parents!")
                print("You lost. Better luck next time!")
                print()
                done = True
    if current_room == 6:
        search = input("Would you like to search the guest room? ")
        print()
        if search.upper() == "Y" or search.upper() == "YES":
            print("You found the key! It is on the covers, but the mother is sleeping under them.")
            print("Be quiet and don't let her catch you if you want to grab it.")
            print()
            print("You have two options: 1 - Grab the key off the covers carefully")
            print("Or 2 - Tickle her nose to get her to move and knock the key off the bed")
            escape = int(input("Option 1 or Option 2? "))
            print()
            if escape == 1:
                print("Good decision! The mother is a deep sleeper. You didn't wake her.")
                print("Move to the next room, so you can escape!")
                print()
                key_found+=1
            elif escape == 2:
                print("Bad decision! The mother is a deep sleeper. You didn't wake her, and the father found you!")
                print("You lost. Better luck next time!")
                print()
                done = True
    if current_room == 7 and key_found == 1:
        print("You escaped! Congratulations!")
        print()
        done = True