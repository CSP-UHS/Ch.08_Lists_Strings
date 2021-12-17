'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import time
K = 2
C = 4
d1 = 12
flash = 0

BH = 0
dumb = 0
print("")
once = 0
room_list = []
# Create rooms and add to room list
print("You are in the bedroom and you wake up to a loud noise.")
print("You see your dog looking up to you.")
print("Something seems off.")
room = ["You are in the bedroom. W",None,None,None,1,0] #NESW #0
room_list.append(room)

room = ["You are in the living room. NESW",3,d1,d1,d1,1]#10 - the whole in the wall #1
room_list.append(room)

room = ["You are in the kitchen. NS",1,None,5,None,2] #2
room_list.append(room)

room = ["You are in the bathroom. S",None,None,1,None,3] #3
room_list.append(room)

room = ["You are in storage room. ES",None,1,9,None,4]#4
room_list.append(room)

room = ["You are the modern hallway. NS",K,None,6,None,5]#5
room_list.append(room)

room = ["You are in the heating room. NW",None,None,None,7,6]#6
room_list.append(room)

room = ["You are in the A/C room. NE",8,6,None, None,7]#7
room_list.append(room)

room = ["You are in power room. NS",9,None,7,None,8 ]#8
room_list.append(room)

room = ["You are in the creepy hall way. S",C,None,8, None,9]#9
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
            time.sleep(2)
            print("CLICK")
            time.sleep(1)
            print("You hear all the doors lock around you.")
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
            time.sleep(2)
            print("You turn around and see a flash of what looks like a person in the dark.")
            time.sleep(3)
            print("You notice the bathroom door is open.")
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
            print("You notice that the cabinet is open.")
            time.sleep(1.5)
            print("You see what looks to be like a sticky note, A flashlight, sticky tack.")
            time.sleep(2)
            print("You hear a noise behind you.")
            time.sleep(1.5)
            print("Do you want to A. investigate or B. turn around.")
            ans = input("- ")
            if ans.lower() == "b" or ans.lower() == "2" or ans.lower() == "turn around" or ans.lower() == "b.":
                print("You see a person right behind you.")
                time.sleep(2)
                print("After looking for a second they disappear.")
                time.sleep(2)
                print("You wonder if your are just seeing things.")
                time.sleep(1.5)
                print("You turn back around to see only an note card.")
                time.sleep(2)
                print("You look at the sticky note.")
                time.sleep(2)
                print("It has a 3917 writen on it.")
                time.sleep(5)
                print("As you read the sticky note you hear the door slam behind you.")
                time.sleep(5)
                print("You look around in the bathroom.")
                time.sleep(4)
                print("You find a heating vent.")
                time.sleep(2)
                print("You hear the screams get louder.")
                time.sleep(3)
                print("Do you A. kick down the locked door or B. go through the vent?")
                ans = input("-")
                if ans.lower() == "a" or ans.lower() == "1" or ans.lower() == "a." or ans.lower() == "door":
                    print("You kick down the door.")
                    time.sleep(2)
                    print("You stare out into the darkness")
                    time.sleep(4)
                    print("You died")
                    done = True
                    break
                elif ans.lower() == "b" or ans.lower() == "2" or ans.lower() == "b." or ans.lower() == "vent":
                    print("You bash open the vent.")
                    time.sleep(2)
                    print("The screams slowly start to fade away")
                    time.sleep(2)
                    print("as you crawl through the vent away from the bathroom.")
                    time.sleep(4)
                    print("* * *")
                    time.sleep(2)
                    print("After crawling in the vent for awhile the sounds have stopped.")
                    time.sleep(3)
                    print("You finally find another vent opening.")
                    time.sleep(3)
                    print("As you get closer to the vent port, you start hearing noises again.")
                    time.sleep(4)
                    print("You think the noise are coming from farther down the vent, but you are not sure.")
                    time.sleep(4)
                    print("Do you want to, A. leave the vent or B. continue down the vent?")
                    ans = input("-")
                    if ans.lower() == "a" or ans.lower() == "1":
                        print("You find your self in a creepy looking hall way.")
                        time.sleep(3)
                        print("Through the darkness you barly see the numbers darkly writen on the wall 754321")
                        time.sleep(3)
                        print("For some reason the number sequence seems off. It's missing something.")
                        time.sleep(3)
                        print("You hear the sound getting closer where do you go?")
                        C = 21
                        K = 21
                        current_room = 9
                    elif ans.lower() == "b" or ans.lower() == "2":
                        print("You continue down the vent the sounds get louder and louder.")
                        print("The sounds stop.")
                        print("You see a figure right in front of you.")
                        print("You died")
                        done = True
                        break

                elif ans.lower() == "n" or ans.lower() == "no":
                    pass
                #-----------------------------------------------------------
            elif ans.lower() == "a" or ans.lower() == "i" or ans.lower() == "a.":
                print("You hear the sounds turn into screams.")
                time.sleep(2)
                print("You reach for the items")
                time.sleep(2)
                print("Which item will you grab.")
                time.sleep(2)
                print("A. the sticky note, B. the flashlight, or C. THE ONE AND ONLY STICKY TaCK! ")
                ans = input("-")
                if ans.lower() == "sticky note" or ans.lower() == "a." or ans.lower() == "a" or ans.lower() == "1":
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
                elif ans.lower() == "b." or ans.lower() == "b" or ans.lower() == "f" or ans.lower() == "flashlight":
                    flash = 1
                    print("You grab the flashlight as fast as you can and shine it where you hear the screams.")
                    time.sleep(2)
                    print("Only to find the door that you've entered through has been locked behind you.")
                    time.sleep(2)
                    print("You look around in the bathroom.")
                    time.sleep(2)
                    print("You find a heating vent.")
                    time.sleep(2)
                    print("You hear the screams get louder and your flashlight starts flickering.")
                    time.sleep(3)
                    print("Do you A. kick down the locked door or B. go through the vent?")
                    ans = input("-")
                    if ans.lower() == "a" or ans.lower() == "door" or ans.lower() == "a." or ans.lower() == "1":
                        print("You kick down the door.")
                        time.sleep(2)
                        print("You flashlight flickers out.")
                        time.sleep(2)
                        print("You stare out into the darkness")
                        time.sleep(4)
                        print("You died")
                        done = True
                        break
                    elif ans.lower() == "vent" or ans.lower() == "b" or ans.lower() == "b." or ans.lower() == "2":
                        print("You bash open the vent.")
                        time.sleep(2)
                        print("Your flash light becomes even dimmer.")
                        time.sleep(3)
                        print("As you crawl through the vent away from the bathroom your flashlight stops flickering.")
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
                        print("Will you A. leave the vent or B. continue down the vent?")
                        ans = input("-")
                        if ans.lower() == "a" or ans.lower() == "a.":
                            print("You find your self in a creepy looking hall way.")
                            time.sleep(3)
                            print("You shine the flashlight around though the darkness.")
                            time.sleep(3)
                            print("You see rust and mold across the walls and floor.")
                            time.sleep(3)
                            print("You shine your flashlight to the walls and find 754321 writen in red across the wall.")
                            time.sleep(5)
                            print("Something seems wrong about the sequence. It's missing something.")
                            time.sleep(3)
                            print("Then you hear the sounds getting closer where do you go?")
                            C = 21
                            K = 21
                            current_room = 9

                        elif ans.lower() == "b" or ans.lower() == "2":
                            print("You continue down the vent the sounds get louder and louder.")
                            time.sleep(3)
                            print("The sounds stop.")
                            time.sleep(3)
                            print("You see a figure right in front of you.")
                            time.sleep(7)
                            print("You died")
                            done = True
                            break

                elif ans.lower() == "c" or ans.lower() == "tack" or ans.lower() == "c." or ans.lower() == "3":
                    time.sleep(2)
                    print("Congradulations!")
                    print("You passed the idot test!")
                    time.sleep(4)
                    print("You would never survive in a real intruder situation.")
                    print("You died")
                    done = True
                    break
    if rom == 8:
        print("You are in the electricity room.")
        time.sleep(2)
        print("You see a random number pad.")
        time.sleep(3)
        print("The screaming sound become louder.")
        time.sleep(3)
        print("Do you A. attempt the code or B. run.")
        ans = input("-")
        if ans.lower() == "1" or ans.lower() == "a." or ans.lower() == "code" or ans.lower() == "a":
            code = input("Code- ")
            if code == "7654321":
                print("The light blinks green.")
                time.sleep(3)
                print("A secret door opens up from the wall.")
                time.sleep(3)
                print("You run out side away form your house. ")
                time.sleep(3)
                print("Then you realise you left your dog.")
                time.sleep(6)
                print("but you are just mostly glad to be alive.")
                time.sleep(3)

                print("YOU WON")
                print("ENDING 1- My sister ending")
                done = True
                break
            else:
                print("The sounds get louder")
                time.sleep(3)
                print("The light blinks red")
                time.sleep(6)
                print("You turn around to see the figure right in front of you.")
                time.sleep(7)
                print("You died.")
                done = True
                break

        elif ans.lower() == "b" or ans.lower() == "b." or ans.lower() == "2" or ans.lower() == "run":
            print("You run as fast as you can away from the sound. You start to out run the noise.")
            time.sleep(5)
            print("But then, just as you are trying to run out of the heating room.")
            time.sleep(3)
            print("The door your running to slams closed and locks.")
            time.sleep(3)
            print("You hear the noise coming to you")
            time.sleep(3)
            print("You see a weird human looking figure turn the corner.")
            time.sleep(3)
            print("What will you do?")
            time.sleep(2)
            print("A. prepare to fistfight the intruder, B. Use your flashlight, C. Say a joke?")
            current_room = 6
            ans = input("-")
            if ans.lower() == "a" or ans.lower() == "1":
                print("You charge the intruder and hear a loud bang. You still landed a punch in their face.")
                time.sleep(3)
                print("You then realise they had a gun.")
                time.sleep(3)
                print("You died, at least you made an effort.")
                done = True
                break
            elif ans.lower() == "b" or ans.lower() == "2":
                print("Click on the flashlight and nothing happens.")
                time.sleep(3)
                print("The figure starts to raise their arm.")
                time.sleep(3)
                print("In a last ditch effort you will?")
                time.sleep(3)
                print("A. Throw the flashlight. B. falcon punch.")
                ans = input("-")
                if ans.lower() == "a" or ans.lower() == "1":
                    print("You throw the flashlight.")
                    time.sleep(5)
                    print("You see the flash light nail the figure in the head")
                    time.sleep(6)
                    print("The figure drops to the ground.")
                    time.sleep(2)
                    print("You Won!")
                    time.sleep(1)
                    print("Ending 2- Your dog will be glad to see you")
                    done = True
                    break
                elif ans.lower() == "b" or ans.lower() == "2":
                    print("You sprint at the intruder.")
                    time.sleep(2)
                    print("You see a flash and a hear a bang.")
                    time.sleep(3)
                    print("The intruder shot you down.")
                    time.sleep(3)
                    print("You died.-you were so close!")
                    done = True
                    break
            elif ans.lower() == "c" or ans.lower() == "3":
                print("You say- wats 9 + 10?")
                time.sleep(3)
                print("The intruder responded with a gunshot.")
                time.sleep(6)
                print("You died. 21?")
                done = True
                break

    print()
    print(room_list[current_room][0])
    bing = input("Type N,E,W,S, directions or Q to quit. - ")
    #North
    if bing.lower() == "n" or bing.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way!")
        elif next_room == 21:
            print("The door is welded shut.")
        else:
            current_room = next_room
    #East
    elif bing.lower() == "e" or bing.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way!")
        elif next_room == 12:
            print("The door is locked.")
        else:
            current_room = next_room
    #West
    elif bing.lower() == "w" or bing.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way!")
        elif next_room == 12:
            print("The door is locked")
        else:
            current_room = next_room
    #South
    elif bing.lower() == "s" or bing.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way!")
        elif next_room == 12:
            print("The door is locked.")
        elif next_room == 12:
            print("The door is welded shut.")
        else:
            current_room = next_room
    #Quit
    elif bing.lower() == "q" or bing.lower() == "quit":
        done = True

    #Stupid
    else:
        print("Not sure you understand what you are doing???")
