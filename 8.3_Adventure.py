'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game


'''
done=False;current_room=0;var=0;wait=False;key=0;pc=0;dead=False;key_used=0
room_list=[]
#First Floor
#0
room=["You are in a main hall. There is a statue in the corner and doors to the North, East, and West.",3,5,None,1]
room_list.append(room)
#1
room=["You are in a living room. There is a couch with a table by it as well as a bookshelf along the far wall. The only door is back the way you came",None,0,None,None]
room_list.append(room)
#2
room=["You are in a living room. There is recliner with an endtable next to it as well as a TV showing static. The only door is back the way you came  ",None,3,None,None]
room_list.append(room)
#3
room=["you enter A hall. There is a stairway to the North, and doors to the East, South, and West",6,4,0,2]
room_list.append(room)
#4
room=["You are in a dining room, There is a table in the center that seems to be set for dinner with no one around. There are doors to the South and West",None,None,5,3]
room_list.append(room)
#5
room=["You are in a kitchen. The counters are spotless, but the fridge is slightly open. There are doors to the North and West",4,None,None,0]
room_list.append(room)
#Second Floor
#6
room=["You are in a hallay. There is a painting on the floor. There is a door to the West and stairs going down to the South",None,None,3,7]
room_list.append(room)
#7
room=["You are in a hangout room. There are sofas in a circle and doors to the North, and East.",8,6,None,None]
room_list.append(room)
#8
room=["You are in a hallway. There is a small hole on the west wall. There are doors to the East and South.",None,9,7,None]
room_list.append(room)
#9
room=["You are in a master bedroom. There is a bookshelf above the bed. There are doors to the North and West.",10,None,None,8]
room_list.append(room)
#10
room=["You are in a bathroom. There is a hot tub, shower and sink. On the sink there is a crowbar. The only door is back the way you came.",None,None,9,None]
room_list.append(room)


print("Welcome to Abandoned house. In this game you will be asked a few questions. if it is a yes or no question, you can reply with y, n, Yes, No, yes, no, or any thing that has to do with yes or no.0")
print("When being asked what direction to go you can either say N E S W or north east south west")
while dead==False:
    while done==False:
        if current_room==0:
            print()
            print(room_list[current_room][0])
            var=current_room
            if key_used==1:
                break
            if key==1:
                while wait==False:
                    exit=input("Would you like to use the key on the front door?")
                    if exit.lower()=="yes" or exit.lower()=="y":
                        done=True
                        key_used=1
                        break

            else:
                while wait==False:
                    user=input('Would you like to inspect the statue?')
                    if user.lower()=="yes" or user.lower()=="y":
                        print("its an empty statue. Kinda useless")
                        break
                    elif user.lower()=="no" or user.lower()=="n":
                        break
                    else:
                        print("Not an option")
                wait=False
                while wait==False:
                    direction=input("Which way would you like to go? North, South, East, or West?")
                    if direction.lower()=="north" or direction.lower()=="n":
                        if room_list[var][1]==None:
                            print("There is no door that way")
                        else:
                            current_room=room_list[current_room][1]
                            break
                    elif direction.lower()=="east" or direction.lower()=="e":
                        if room_list[var][2]==None:
                            print("There is no door that way")
                        else:
                            current_room=room_list[var][2]
                            break
                    elif direction.lower()=="south" or direction.lower()=="s":
                        if room_list[var][3]==None:
                            print("There is no door that way")
                        else:
                            current_room=room_list[var][3]
                            break
                    elif direction.lower()=="west" or direction.lower()=="w":
                        if room_list[var][4]==None:
                            print("There is no door that way")
                        else:
                            current_room=room_list[var][4]
                            break
        if current_room==1:
            print()
            print(room_list[current_room][0])
            var = current_room
            while wait == False:
                user = input('Would you like to look at the bookcase?')
                if user.lower() == "yes" or user.lower() == "y":
                    print("you find a paper clip")
                    pc=1
                    break
                elif user.lower() == 'no' or user.lower() == "n":
                    break
                else:
                    print("Not an option")
            wait = False
            while wait == False:
                direction = input("Which way would you like to go? North, South, East, or West?")
                if direction.lower() == "north" or direction.lower() == "n":
                    if room_list[var][1] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[current_room][1]
                        break
                elif direction.lower() == "east" or direction.lower() == "e":
                    if room_list[var][2] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][2]
                        break
                elif direction.lower() == "south" or direction.lower() == "s":
                    if room_list[var][3] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][3]
                        break
                elif direction.lower() == "west" or direction.lower() == "w":
                    if room_list[var][4] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][4]
                        break
        if current_room==2:
            print()
            print(room_list[current_room][0])
            var = current_room
            while wait == False:
                user = input('Would you like to look at the chair?')
                if user.lower() == "yes" or user.lower() == "y":
                    print("You sit on the chair. It is really comfy")
                    break
                elif user.lower() == 'no' or user.lower() == "n":
                    break
                else:
                    print("Not an option")
            wait = False
            while wait == False:
                direction = input("Which way would you like to go? North, South, East, or West?")
                if direction.lower() == "north" or direction.lower() == "n":
                    if room_list[var][1] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[current_room][1]
                        break
                elif direction.lower() == "east" or direction.lower() == "e":
                    if room_list[var][2] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][2]
                        break
                elif direction.lower() == "south" or direction.lower() == "s":
                    if room_list[var][3] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][3]
                        break
                elif direction.lower() == "west" or direction.lower() == "w":
                    if room_list[var][4] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][4]
                        break
        if current_room==3:
            print()
            print(room_list[current_room][0])
            var = current_room
            wait = False
            while wait == False:
                direction = input("Which way would you like to go? North, South, East, or West?")
                if direction.lower() == "north" or direction.lower() == "n":
                    if room_list[var][1] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[current_room][1]
                        break
                elif direction.lower() == "east" or direction.lower() == "e":
                    if room_list[var][2] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][2]
                        break
                elif direction.lower() == "south" or direction.lower() == "s":
                    if room_list[var][3] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][3]
                        break
                elif direction.lower() == "west" or direction.lower() == "w":
                    if room_list[var][4] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][4]
                        break
        if current_room==4:
            print()
            print(room_list[current_room][0])
            var = current_room
            while wait == False:
                user = input('Would you like to look at the Table?')
                if user.lower() == "yes" or user.lower() == "y":
                    print("The table comes to life and eats you.")
                    dead=True
                    done=True
                    break
                elif user.lower() == 'no' or user.lower()== "n":
                    break
                else:
                    print("Not an option")
            if dead==True or done==True:
                break
            wait = False
            while wait == False:
                direction = input("Which way would you like to go? North, South, East, or West?")
                if direction.lower() == "north" or direction.lower() == "n":
                    if room_list[var][1] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[current_room][1]
                        break
                elif direction.lower() == "east" or direction.lower() == "e":
                    if room_list[var][2] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][2]
                        break
                elif direction.lower() == "south" or direction.lower() == "s":
                    if room_list[var][3] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][3]
                        break
                elif direction.lower() == "west" or direction.lower() == "w":
                    if room_list[var][4] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][4]
                        break
        if current_room==5:
            print()
            print(room_list[current_room][0])
            var = current_room
            while wait == False:
                user = input('Would you like to inspect the fridge?')
                if user.lower() == "yes" or user.lower() == "y":
                    print("It's an empty fridge that no longer works")
                    break
                elif user.lower() == 'no' or user.lower() == "n":
                    break
                else:
                    print("Not an option")
            wait = False
            while wait == False:
                direction = input("Which way would you like to go? North, South, East, or West?")
                if direction.lower() == "north" or direction.lower() == "n":
                    if room_list[var][1] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[current_room][1]
                        break
                elif direction.lower() == "east" or direction.lower() == "e":
                    if room_list[var][2] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][2]
                        break
                elif direction.lower() == "south" or direction.lower() == "s":
                    if room_list[var][3] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][3]
                        break
                elif direction.lower() == "west" or direction.lower() == "w":
                    if room_list[var][4] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][4]
                        break
        if current_room==6:
            print()
            print(room_list[current_room][0])
            var = current_room
            while wait == False:
                user = input('Do you pick up the painting?')
                if user.lower() == "yes" or user.lower() == "y":
                    print("You find a nickel, nice!")
                    break
                elif user.lower() == 'no' or user.lower() == "n":
                    break
                else:
                    print("Not an option")
            wait = False
            while wait == False:
                direction = input("Which way would you like to go? North, South, East, or West?")
                if direction.lower() == "north" or direction.lower() == "n":
                    if room_list[var][1] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[current_room][1]
                        break
                elif direction.lower() == "east" or direction.lower() == "e":
                    if room_list[var][2] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][2]
                        break
                elif direction.lower() == "south" or direction.lower() == "s":
                    if room_list[var][3] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][3]
                        break
                elif direction.lower() == "west" or direction.lower() == "w":
                    if room_list[var][4] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][4]
                        break
        if current_room == 7:
            print()
            print(room_list[current_room][0])
            var = current_room
            while wait == False:
                user = input('Would you like to sit down and hang out?')
                if user.lower() == "yes" or user.lower() == "y":
                    print("You hang for a bit and get a feeling there is another being in the room with you.")
                    break
                elif user.lower() == 'no' or user.lower() == "n":
                    break
                else:
                    print("Not an option")
            wait = False
            while wait == False:
                direction = input("Which way would you like to go? North, South, East, or West?")
                if direction.lower() == "north" or direction.lower() == "n":
                    if room_list[var][1] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[current_room][1]
                        break
                elif direction.lower() == "east" or direction.lower() == "e":
                    if room_list[var][2] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][2]
                        break
                elif direction.lower() == "south" or direction.lower() == "s":
                    if room_list[var][3] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][3]
                        break
                elif direction.lower() == "west" or direction.lower() == "w":
                    if room_list[var][4] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][4]
                        break
        if current_room==8:
            print()
            print(room_list[current_room][0])
            var = current_room
            if pc==1:
                while wait==False:
                    hole=input("Would you like to use the paperclip on the hole?")
                    if hole.lower()=="yes" or hole.lower()=="y":
                        print("You open a secret door and find a bunch of dead bodies. Looks like you found the owners...")
                    else:
                        break
                    break
            wait = False
            while wait == False:
                direction = input("Which way would you like to go? North, South, East, or West?")
                if direction.lower() == "north" or direction.lower() == "n":
                    if room_list[var][1] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[current_room][1]
                        break
                elif direction.lower() == "east" or direction.lower() == "e":
                    if room_list[var][2] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][2]
                        break
                elif direction.lower() == "south" or direction.lower() == "s":
                    if room_list[var][3] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][3]
                        break
                elif direction.lower() == "west" or direction.lower() == "w":
                    if room_list[var][4] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][4]
                        break
        if current_room==9:
            print()
            print(room_list[current_room][0])
            var = current_room
            while wait == False:
                user = input('Would you like to inspect the bookshelf?')
                if user.lower() == "yes" or user.lower() == "y":
                    print("There are books on canabalism... creepy\n There is also a key on the bookshelf")
                    key=1
                    break
                elif user.lower() == 'no' or user.lower() == "n":
                    break
                else:
                    print("Not an option")
            wait = False
            while wait == False:
                direction = input("Which way would you like to go? North, South, East, or West?")
                if direction.lower() == "north" or direction.lower() == "n":
                    if room_list[var][1] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[current_room][1]
                        break
                elif direction.lower() == "east" or direction.lower() == "e":
                    if room_list[var][2] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][2]
                        break
                elif direction.lower() == "south" or direction.lower() == "s":
                    if room_list[var][3] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][3]
                        break
                elif direction.lower() == "west" or direction.lower() == "w":
                    if room_list[var][4] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][4]
                        break
        if current_room==10:
            print()
            print(room_list[current_room][0])
            var = current_room
            while wait == False:
                user = input('Would you like to take a bath?')
                if user.lower() == "yes" or user.lower() == "y":
                    print("You take a bath in the empty weird house. Congrat weirdo...")
                    break
                elif user.lower() == 'no' or user.lower() == "n":
                    break
                else:
                    print("Not an option")
            wait = False
            while wait == False:
                direction = input("Which way would you like to go? North, South, East, or West?")
                if direction.lower() == "north" or direction.lower() == "n":
                    if room_list[var][1] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[current_room][1]
                        break
                elif direction.lower() == "east" or direction.lower() == "e":
                    if room_list[var][2] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][2]
                        break
                elif direction.lower() == "south" or direction.lower() == "s":
                    if room_list[var][3] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][3]
                        break
                elif direction.lower() == "west" or direction.lower() == "w":
                    if room_list[var][4] == None:
                        print("There is no door that way")
                    else:
                        current_room = room_list[var][4]
                        break
    break
if dead==True:
    print("You died!")
else:
    print("Congrats! you did the good of getting out!")