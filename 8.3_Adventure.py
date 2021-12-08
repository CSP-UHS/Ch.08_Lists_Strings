'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import time
dumb = 0
print("")
once = 0
room_list = []
# Create rooms and add to room list
room = ["You are the bedroom and you wake up to a loud noise."
        "You see your dog looking up to you."
        "Something seems off. W",None,None,None,1,0 ] #NESW #0
room_list.append(room)

room = ["You are in the living room.",3,0,2,4,1]#10 - the whole in the wall #1
room_list.append(room)

room = ["You are in the kitchen",1,None,5,None,1] #2
room_list.append(room)

room = ["You are in the bathroom",None,None,1,None,""] #3
room_list.append(room)

room = ["You are in storage room",None,1,9,None,""]#4
room_list.append(room)

room = ["You are the modern hallway",2,None,6,None,""]#5
room_list.append(room)

room = ["You are in the heating room",5,None,None,7,""]#6
room_list.append(room)

room = ["You are in the A/C room",8,6,None, None,""]#7
room_list.append(room)

room = ["You are in power room",9,None,7,None,"" ]#8
room_list.append(room)

room = ["You are in the creepy hall way",4,None,8, None]#9
room_list.append(room)





current_room = 0
done = False
while not done:
    if current_room == 1:
        if once == 0:
            once += 1
            print("You walk into the living room.")
            time.sleep(.5)
            print("You notice the lights are out")
            time.sleep(.5)
            print("You also notice a black shot on the wall.")
            time.sleep(.5)
            print("Do you wish to inspect? y/n")
        if ans.lower() == "y" or ans.lower() == "yes":
            print("You walk closer to the wall.")
            print("It looks like a hole as you get closer you hear a noise behind you.")
            print("You turn around and see a flash of what looks like a person in the dark.")
            dumb += 1
            pass
        elif ans.lower() == "y" and dumb == 1 or ans.lower() == "yes" and dumb == 1:
            print("You slowly walk closer to the wall.")
            print("It looks like a hole but as you get near it, you hear scream behind you.")
            print("You turn around and see a flash of what looks like a person in the dark wearing a cloak.")
            dumb += 1
            pass
        elif ans.lower() == "y" and dumb == 1 or ans.lower() == "yes" and dumb == 2:
            print("You slowly walk closer to the wall.")
            print("It looks like a hole but as you get near it, you notice its a blood stain.")
            print("You turn around and see a flash of what looks like a person right in front of you.")
            print("You died")
            done = True
            break
        elif ans.lower() == "n" or ans.lower() == "no":
            continue
        else:
            print("Why?")
            pass

    rom = room_list[current_room][5]
    if rom == ""



    print()
    print(room_list[current_room][0])
    bing = input("Type N,E,W,S,",I ,"directions or Q to quit")
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
