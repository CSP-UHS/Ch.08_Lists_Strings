import sys
print("\033[7;30;49m The year is 2099 and the entire universe is owned by FaceBook.")
print("Earth is a nuclear wasteland after nuclear war broke out after Mark Zuckerberg blocked out the sun.")
print("You are one of the last people in the world that didn't upload your brain to the internet.")
print("Everybody and everything you used to know has been turned into mindless FaceBook robots.")
print("You have snuck into Mark Zuckerberg's secret mansion because it is the last place in the world that has water")
print("Your goal is to finesse a jug of water from Mark Zuckerberg's mansion before he turns you into a facebook robot.")
print()
print("You have a radar that shows how far Zuckerberg is from his estate.")
print("He starts 120 minutes away and every room move you make he travels about 5 minutes")
# 0=FrontPorch 1=MainHall 2=ZuccsBedroom 3=ZuccsOffice 4=ZuccsDiningRoom 5=SafeRoom 6=MeetingRoom
# Create Rooms and add to room list
room_list = []
room = ["\033[0;38;49m You are on the Front Porch.", 1, None, None, None]
room_list.append(room)
room = ["\033[0;36;49mYou are in the Art Gallery.", 5, 4, 0, 2]
room_list.append(room)
room = ["\033[0;33;49m You are in Zuckerberg's Bedroom.", 3, 1, None, None]
room_list.append(room)
room = ["\033[0;32;49m You are in Zuckerberg's Office", None, None, 2, None]
room_list.append(room)
room = ["\033[0;31;49m You are in Zuckerberg's Dining Room.", 6, None, None, 1]
room_list.append(room)
room = ["\033[0;35;49m You are in the Zuckerberg's Safe Room.", None, None, 1, None]
room_list.append(room)
room = ["\033[0;34;49m You are in the Meeting Room, There is a big screen covering the entire Northern Wall", None, None, 4, None]
room_list.append(room)
current_room = 0

backpack = []

#Office Desk Key
key1 = 0
keyr = 0
zp = 0
done = False
zuckdist = 120

while not done:
    print()
    print(room_list[current_room][0])
    bing = input("Type N, E, W, or S for direction, type T to check how long you have, type B to check your backpack, type I if you want to inspect the room, or type Q to quit\n")

    # ZUCK TIMER
    if zuckdist < 0:
        print("\033[7;31;49m")
        print("You hear Zuck arrive in his 2010 Nissan Maxima! You're done for!!!")
        sys.exit()


    #INSPECT
    if bing.lower() == "i" or bing.lower() == "inspect":
        print("You have chosen to inspect the room...")
        #FRONT PORCH
        if current_room == 0:
            print("There is nothing to inspect")
        #MAIN HALL
        if current_room == 1:
            print("There are many paintings and sculptures in the art gallery, \nYou notice one of the paintings is torn in the corner.")
            answer1 = input("Would you like to peel it back?: Y or N \n")
            if answer1.lower() == "y" or answer1.lower() == "yes":
                print("You discovered a key taped on the crusty wall behind the painting, \nIt is labeled with the words 'Office Desk'. \nYou throw it in your backpack.")
                backpack.append("Office Desk Key")
                print(backpack)
                key1 += 1
            else:
                print("You selected to not check it")

        #ZUCKERBERG BEDROOM
        if current_room == 2:
            print("You notice that the only two things in Zuckerberg's bedroom are a small dresser and a tiny twin sized bed.")
            answer2 = input("Would you like to search through the small dresser?: Y or N \n")
            if answer2.lower() == "y" or answer2.lower() == "yes":
                print("After perusing through the dresser you find nothing besides a couple gum wrappers and lots of dust")
                answer22 = input("Do you pull out the dresser drawers in frustration?: Y or N \n")
                if answer22.lower() == "y" or answer22.lower() == "yes":
                    print("After carefully inspecting the back of each individual drawer you find a sticky note on the back of the top one. \nThe sticky note says 'hahaha you wasted your time' What the hell were you thinking why would there be something hidden behind the dresser?!?!?!? \nZuck got 15 miles closer during the wasted time...\n")
                    zuckdist -= 15
                else:
                    print("You selected to not check it")
            else:
                print("You selected not to check it")

        #ZUCKERBERG OFFICE
        if current_room == 3:
            print("For whatever reason Zuckerberg has a double decker desk with like a million drawers. \nOnly one of the drawers is locked.")
            if key1 == 1:
                answer3 = input("Would you like to use your Office Desk Key?: Y or N\n")
                if answer3.lower() == "y" or answer3.lower() == "yes":
                    print("You used your key to unlock the locked drawer and find a padlock key... \nThe Key is labeled 'Dining Room'.")
                    keyr += 1
                    backpack.append("Key Ring")
                else:
                    print("You decided not to use the key for some reason")
            else:
                print()
                print("You need a key for the locked drawer!!!")

        #ZUCKERBERG DINING ROOM
        if current_room == 4:
            print("\nYou enter the Dining Room and at first it looks normal but then you go to munch on one of the apples on the counter and notice it is made from plastic. \nYou realize that Mark has no real food in his home because he is a cyborg lizard person \n")
            print("You see a picture frame chained down to the counter with a photo of Mark Zuckerberg surfing that is kept there by a padlock.")
            if keyr == 1:
                answer4 = input("Would you like to use your Padlock Key?: Y or N\n")
                if answer4.lower() == "y" or answer4.lower() == "yes":
                    print("The padlock key opened the padlock and you took the picture of Zuckerberg along with you for company.")
                    zp += 1
                else:
                    print("You decided to not use your Padlock Key...")
            else:
                print("You need some kind of key for the padlock!")

        #ZUCKERBERG MEETING ROOM
        if current_room == 6:
            print("You notice a face scanner on the opposite wall from the big screen")
            if zp == 1:
                answer6 = input("Would you like to hold the picture of Zuckerberg up to the face scanner?\n")
                if answer6.lower() == "y" or answer6.lower() == "yes":
                    print("As you hold up the picture of Zuckerberg to the scanner, the large screen on the opposite wall displays the code '3269'")
            else:
                print("You need Zuck's likeness in order to use the face scanner...")

        #SAFE ROOM
        if current_room == 5:
            print("\n There is a big safe in the middle of the room. \n It is labeled 'WATER JUGS' and there is a code lock on it.")
            codeinput = input("ENTER CODE: ")
            if codeinput == "3269":
                print("ACCESS GRANTED")
                print("After the safe opens you throw the jug of water into your backpack and book it out the front door")
                print("You made it out with Zuckerberg only", zuckdist, "miles away!")
                done = True
            else:
                print("INCORRECT CODE")
                zuckdist -= 30

    # BACKPACK
    if bing.lower() == "b" or bing.lower() == "backpack":
        print("Your backpack contains:", backpack)

    # NORTH
    if bing.lower() == "n" or bing.lower() == "north":
        zuckdist -= 5
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You cannot go that way")
        else:
            current_room = next_room
    # EAST
    if bing.lower() == "e" or bing.lower() == "east":
        zuckdist -= 5
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You cannot go that way")
        else:
            current_room = next_room
    # SOUTH
    if bing.lower() == "s" or bing.lower() == "south":
        zuckdist -= 5
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You cannot go that way")
        else:
            current_room = next_room
    # WEST
    if bing.lower() == "w" or bing.lower() == "west":
        zuckdist -= 5
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You cannot go that way")
        else:
            current_room = next_room
    # TIME
    if bing.lower() == "t" or bing.lower() == "time":
        print("Zuck is", zuckdist, "minutes from getting home to his mansion.")
    #QUIT
    elif bing.lower() == "q" or bing.lower() == "quit":
        print("Thanks for playing!")
        sys.exit()
