'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import time
BH = 0
dumb = 0
print("")
once = 0
room_list = []
# Create rooms and add to room list
print("You are the bedroom and you wake up to a loud noise.")
print("You see your dog looking up to you.")
print("Something seems off.")
room = ["You are the bedroom W.I",None,None,None,1,0] #NESW #0
room_list.append(room)

room = ["You are in the living room. NESW",3,0,2,4,1]#10 - the whole in the wall #1
room_list.append(room)

room = ["You are in the kitchen. NS",1,None,5,None,2] #2
room_list.append(room)

room = ["You are in the bathroom. S",None,None,1,None,3] #3
room_list.append(room)

room = ["You are in storage room. ES",None,1,9,None,4]#4
room_list.append(room)

room = ["You are the modern hallway. NS",2,None,6,None,5]#5
room_list.append(room)

room = ["You are in the heating room. NW",5,None,None,7,6]#6
room_list.append(room)

room = ["You are in the A/C room. NE",8,6,None, None,7]#7
room_list.append(room)

room = ["You are in power room. NS",9,None,7,None,8 ]#8
room_list.append(room)

room = ["You are in the creepy hall way. NS",4,None,8, None,9]#9
room_list.append(room)





current_room = 0
done = False
while not done:
    #---------------------------Living room
    if current_room == 1:
        if once == 0:
            once += 1
            print("You walk into the living room.")
            time.sleep(1)
            print("You notice the lights are out")
            time.sleep(1)
        print("You also notice a black hole on the wall.")
        time.sleep(1)
        print("Do you wish to inspect? y/n")
        ans = input("-")
        if ans.lower() == "y" and dumb == 2 or ans.lower() == "yes" and dumb == 2:
            print("You slowly walk closer to the wall.")
            time.sleep(1)
            print("It looks like a hole but as you get near it, you notice its a blood stain.")
            time.sleep(1)
            print("You turn around and see a flash of what looks like a person right in front of you.")
            time.sleep(3)
            print("You died")
            done = True
            break
        elif ans.lower() == "y" and dumb == 1 or ans.lower() == "yes" and dumb == 1:
            print("You slowly walk closer to the wall.")
            time.sleep(1)
            print("It looks like a hole but as you get near it, you hear scream behind you.")
            time.sleep(1)
            print("You turn around and see a flash of what looks like a person in the dark wearing a cloak.")
            dumb += 1
            pass
        elif ans.lower() == "y" or ans.lower() == "yes":
            print("You walk closer to the wall.")
            time.sleep(1)
            print("It looks like a hole as you get closer you hear a noise behind you.")
            time.sleep(1)
            print("You turn around and see a flash of what looks like a person in the dark.")
            dumb += 1
            pass
        elif ans.lower() == "n" or ans.lower() == "no":
            pass
        else:
            print("Why?")
            pass

    # INTERACTION____________Bathroom_______________________________________
    rom = room_list[current_room][5]
    if rom == 3:
        print("You are in the bathroom.")
        time.sleep(1.5)
        if BH == 0:
            BH = 1
            print("You notice that the cabnet is open.")
            time.sleep(1.5)
            print("You what looks to be like a sticky note, A flashlight, and a key.")
            time.sleep(2)
            print("You hear a noise behind you.")
            time.sleep(1.5)
            print("Do you want to investigate or turn around.")
            ans = input("- ")
            if ans.lower() == "turnaround" or ans.lower() == "turn around" or ans.lower() == "turn" or ans.lower() == "t":
                print("You see a person right behind you.")
                time.sleep(2)
                print("After looking for a second they disappear.")
                time.sleep(2)
                print("You wounder if your are just seeing things.")
                time.sleep(1.5)
                print("You turn back around to see only an note card.")
                time.sleep(2)
                print("Do you with to investigate the objects?")
                ans = input("- ")
                if ans.lower() == "y" or ans.lower() == "yes":
                    print("You look at the sticky note.")
                    time.sleep(2)
                    print("It has a 3917 writen on it.")
                elif ans.lower() == "n" or ans.lower() == "no":
                    pass
                #-----------------------------------------------------------
            elif ans.lower() == "investigate" or ans.lower() == "i" or ans.lower() == "in":
                print("You hear the sounds turn into screams.")
                time.sleep(2)
                print("You reach for the items")
                time.sleep(2)
                print("Which item will you grab.")
                time.sleep(2)
                print("the sticky note, the flashlight, or the key ")
                ans = input("-")
                if ans.lower() == "sticky note" or ans.lower() == "sn" or ans.lower() == "s" or ans.lower() == "sticky":
                    print("Grab the note card as fast as you can.")
                    time.sleep(2)
                    print("You read the sticky note quickly.")
                    time.sleep(2)
                    print("REDRUM")
                    time.sleep(4)
                    print("You look up to see the figure right in front of you")
                    time.sleep(4)
                    print("You died")
                    done = True
                    break
                elif ans.lower() == "flashlight" or ans.lower() == "fl" or ans.lower() == "f" or ans.lower() == "flash":
                    print("You grab the flashlight as fast as you can and shine it where you hear the screams.")
                    time.sleep(2)
                    print("Only to find the door that you entered through has been locked behind you.")
                    time.sleep(2)
                    print("You look around in the bathroom.")
                    time.sleep(2)
                    print("You find a heating vent.")
                    time.sleep(2)
                    print("You hear the screams get louder and you flashlight starts flickering.")
                    time.sleep(3)
                    print("Do you kick down the locked door or go through the vent?")
                    ans = input("-")
                    if ans.lower() == "kick" or ans.lower() == "door" or ans.lower() == "k" or ans.lower() == "d":
                        print("You kick down the door.")
                        time.sleep(2)
                        print("You flashlight flickers out.")
                        time.sleep(2)
                        print("You stare out into the darkness")
                        time.sleep(4)
                        print("You died")
                        done = True
                        break
                    elif ans.lower() == "vent" or ans.lower() == "v" or ans.lower() == "the vent" or ans.lower() == "tv":
                        print("You bash open the vent.")
                        time.sleep(2)
                        print("Your flash light becomes even dimmer.")
                        time.sleep(3)
                        print("As you crawl through the vent away from the bathroom your flashlight stops flickering")
                        time.sleep(4)
                        print("* * *")
                        time.sleep(2)
                        print("After crawling in the vent for awhile.")
                        time.sleep(3)
                        print("You finally find another vent opening.")
                        time.sleep(3)
                        print("As you get closer to the vent port, you start hearing noises again.")
                        time.sleep(4)
                        print("You think the noise are coming from farther down the vent, but you are not sure.")
                        time.sleep(4)
                        print("Will you leave the vent or continue down the vent?")
                        ans = input("-")
                        if ans.lower() == "leave" or ans.lower() == "l":
                            print("You find your self in a creepy looking hall way.")
                            print("You see the numbers 7543")
                            print("You hear the sound getting closer where do you go?")
                            current_room = 9

    print()
    print(room_list[current_room][0])
    bing = input("Type N,E,W,S, directions or Q to quit")
    #North
    if bing.lower() == "n" or bing.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way!")
        else:
            current_room = next_room
    #East
    elif bing.lower() == "e" or bing.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way!")
        else:
            current_room = next_room
    #West
    elif bing.lower() == "w" or bing.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way!")
        else:
            current_room = next_room
    #South
    elif bing.lower() == "s" or bing.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way!")
        else:
            current_room = next_room
    #Quit
    elif bing.lower() == "q" or bing.lower() == "quit":
        done = True

    #Stupid
    else:
        print("Not sure you understand what you are doing???")

'''
|~~~~~~~~~~~~~|
|      []     |
|    [][][]   |
|    ||[]     |
|    ||||     |
|    <>||     |
|    <><>     |
|_____________|
'''
