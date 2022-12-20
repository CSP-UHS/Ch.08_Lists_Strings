'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import random
import time
roomList = ["Place holder"]
#Rooms and basic descriptions
room = ["You are in a blank red room, there is nothing around for you to see or grab.",7,2,4,3]
roomList.append(room)
room = ["You are in a blank green room, there is nothing around for you to see or grab.",8,3,5,1]
roomList.append(room)
room = ["You are in a blank purple room, there is nothing around for you to see or grab.",9,1,6,2]
roomList.append(room)
room = ["You are in a blank blue room, there is nothing around for you to see or grab.",1,5,7,6]
roomList.append(room)
room = ["You are in a blank white room, there is nothing around for you to see or grab.",2,6,8,4]
roomList.append(room)
room = ["You are in a blank orange room, there is nothing around for you to see or grab.",3,4,9,5]
roomList.append(room)
room = ["You are in a blank yellow room, there is nothing around for you to see or grab.",4,8,1,9]
roomList.append(room)
room = ["You are in a blank pink room, there is nothing around for you to see or grab.",5,9,2,7]
roomList.append(room)
room = ["You are in a pitch black room, you cannot see a thing.",6,7,3,8]
roomList.append(room)

currentRoom = 5
x = 0
y = 0
inventory = ["noKey"]

#Main program
done = False

while not done:
    x += 1
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    d = random.randint(1, 9)
    print()
    print(roomList[currentRoom][0])
    print("==============================")
    drct = input("Which direct will you travel? N,E,S, or W. "
                 "You can also use I to interact or Q to quit. What is your choice: ")
    if drct.lower() == "n": #North
        nextRoom = roomList[currentRoom][1]
        currentRoom = nextRoom

    elif drct.lower() == "e": #East
        nextRoom = roomList[currentRoom][2]
        currentRoom = nextRoom

    elif drct.lower() == "s": #South
        nextRoom = roomList[currentRoom][3]
        currentRoom = nextRoom

    elif drct.lower() == "w": #West
        nextRoom = roomList[currentRoom][4]
        currentRoom = nextRoom

    elif drct.lower() == "i": #Interact
        if x >= 5:
            if currentRoom == 1:
                y += 1
                if y >= 5:
                    print("You give up on the key and just break the box.")
                    print("Luckily there is nothing breakable in the box.")
                    print("Just a sheet that says pi.")
            if currentRoom == 2:
                print("Use it in the door.")
            if currentRoom == 3:
                print("Pick up the key.")
            if currentRoom == 4:
                print("Please try to escape.")
            if currentRoom == 5:
                print("You try talk to her but as you blink she disappears. Maybe she'll be back.")
            if currentRoom == 6:
                print("Hello this is the voice in your head, go to the yellow room..")
            if currentRoom == 7:
                print("You pick up the key. Lets see what its for.")
                inventory[0] = "Key"
            if currentRoom == 8:
                code = int(input("What is the code: "))
                if code == 3141:
                    print("You open the box but there is nothing inside.")
                else:
                    print("That is not the code try again. I'm hungry.")
            if currentRoom == 9:
                if inventory[0] == "Key":
                    print("You open the door to escape this place and see a blinding white light.")
                    print("You wake up in a blank white room as you look "
                          "around you see your back to the start.")
                    print("This place will never end and you will never escape.")
                    x = 0
                    y = 0
                    currentRoom = 5
                    inventory[0] = 0
                else:
                    print("You can't open the door, I guess your still stuck here.")
        else:
            print("There is nothing to interact with. Choose again.")

    elif drct.lower() == "q": #Quit
        print("You close your eyes hoping this is a dream, "
              "but when you open them you are still standing in the same place.")
    else:
        print("Choose again")
    if x >= 5:
        roomList[1] = ["In the red room you now see a box with a lock on the front.",a,b,c,d]
        roomList[2] = ["A number painted in the middle of the green room. 8",a,b,c,d]
        roomList[3] = ["A number painted in the middle of the purple room. 6",a,b,c,d]
        roomList[4] = ["A number painted in the middle of the blue room. 9",a,b,c,d]
        roomList[5] = ["You see a woman standing in the middle of the white room. " \
                         "She gives you a note that tells you not to trust anything.",a,b,c,d]
        roomList[6] = ["A number painted in the middle of the orange room. 3",a,b,c,d]
        roomList[7] = ["You see a key in the yellow room, I wonder what it goes to.",a,b,c,d]
        roomList[8] = ["You see a key pad in the pink room. Let's see what the combination is.",a,c,b,d]
        roomList[9] = ["The lights have turned on and you see a door. " \
                         "Its blended into the black paint of the room.",a,b,c,d]
print("++++++++++++++++++++++++++++++")
print("You played my game. Had fun?")